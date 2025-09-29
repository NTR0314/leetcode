from typing import List, Dict, Tuple
from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        
        # The master queue's only job is to know the overall oldest packet.
        self.package_queue: deque = deque()
        
        # This dictionary's only job is to make getCount fast.
        # It maps: destination -> [list_of_packets, head_pointer_index]
        self.packages_by_dest: Dict[int, List] = defaultdict(lambda: [[], 0])
        
        # A hash map for O(1) duplicate checks.
        self.packageMap: Dict[Tuple, bool] = {}
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet_id = (source, destination, timestamp)
        if packet_id in self.packageMap:
            return False

        # If memory is full, remove the oldest packet from the system.
        if len(self.package_queue) >= self.memoryLimit:
            # 1. Use the master deque to find the oldest packet (O(1)).
            s_old, d_old, t_old = self.package_queue.popleft()
            self.packageMap.pop((s_old, d_old, t_old))
            
            # 2. "Remove" it from the query structure by advancing its head (O(1)).
            self.packages_by_dest[d_old][1] += 1

        # Add the new packet to both data structures.
        self.package_queue.append(packet_id)
        self.packageMap[packet_id] = True
        self.packages_by_dest[destination][0].append(packet_id) # Append to the list
        
        return True

    def forwardPacket(self) -> List[int]:
        if not self.package_queue:
            return []

        # 1. Use the master deque to find and remove the oldest packet (O(1)).
        s, d, t = self.package_queue.popleft()
        self.packageMap.pop((s, d, t))

        # 2. "Remove" it from the query structure by advancing its head (O(1)).
        self.packages_by_dest[d][1] += 1

        return list((s, d, t))

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # Use the specialized query structure for a fast lookup.
        packet_list, head = self.packages_by_dest[destination]

        if head >= len(packet_list):
            return 0

        # Find the start of the time window using binary search (O(log K)).
        # The 'lo=head' parameter is crucial, searching only the "active" packets.
        start_index = bisect.bisect_left(packet_list, startTime, lo=head, key=lambda p: p[2])
        
        # Find the end of the time window.
        end_index = bisect.bisect_right(packet_list, endTime, lo=head, key=lambda p: p[2])
        
        # The number of packets is the difference between the indices.
        return end_index - start_index