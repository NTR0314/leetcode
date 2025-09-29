from functools import cache
from typing import List, Tuple


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def triangulation(i, j) -> int: 
            best = float('inf')
            
            if (j - i) <= 1:
                return 0

            for k in range(i+1, j):
                cur = values[i] * values[k] * values[j]

                tmp = cur + triangulation(i, k) + triangulation(k, j)
                
                if tmp < best:
                    best = tmp

            return int(best)

        ret = triangulation(0, len(values) - 1)
        
        return ret

if __name__ == "__main__":
    s = Solution()
    assert s.minScoreTriangulation([1,2,3]) == 6
    print("Passed test 1\n")
    assert s.minScoreTriangulation([3,7,4,5]) == 144
    print("Passed test 2\n")
    assert s.minScoreTriangulation([1,3,1,4,1,5]) == 13
    print("Passed test 3\n")
            