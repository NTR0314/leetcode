import heapq
from typing import List

class Solution:
    def gain(self, p, t):
        return (t - p) / (t * (t + 1))

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        self.sorted_classes = []
        for p, t in classes:
            heapq.heappush(self.sorted_classes, (-self.gain(p, t), p, t))        
            
        for _ in range(extraStudents):
            print(self.sorted_classes)
            _ , p, t = heapq.heappop(self.sorted_classes)
            p += 1
            t += 1
            heapq.heappush(self.sorted_classes, (-self.gain(p,t), p, t))

        avg_ratio = 0
        for (r, p, t) in self.sorted_classes:
            avg_ratio += p / t
        return avg_ratio / len(classes)
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2))