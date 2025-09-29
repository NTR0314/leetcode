from typing import List
import sys


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        num_pairs = 0
        sorted_points = sorted(points, key=lambda x: (x[0], -x[1]))
        
        print(sorted_points)
        
        for i in range(len(sorted_points) - 1):
            alice_x, alice_y = sorted_points[i]
            max_y = sys.maxsize * -1
            for j in range(i + 1, len(sorted_points)):
                bob_x, bob_y = sorted_points[j]
                print(f"Comparing A({alice_x},{alice_y}) - B({bob_x},{bob_y}), max_y={max_y}")
                if bob_y > max_y and bob_y <= alice_y:
                    print(f"Pair found: A({alice_x},{alice_y}) - B({bob_x},{bob_y})")
                    num_pairs += 1
                    max_y = bob_y
                else:
                    if bob_y < alice_y:
                        max_y = max(max_y, bob_y)
        
        return num_pairs
        