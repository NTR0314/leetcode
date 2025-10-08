from typing import List
import bisect
import math


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()

        def binary_search(array, target: int) -> int:
            left = 0
            right = len(array)

            while left < right:
                middle = (left + right) // 2

                mp = potions[middle]
                if mp >= target:
                    right = middle
                else:
                    left = middle + 1
                    
            return left
        
        # print(f"{potions=}, {success=}")

        ns = len(spells)
        np = len(potions)
        res = [0] * ns
        for i, spell in enumerate(spells):
            sv = math.ceil(success / spell)
            # gi = bisect.bisect_left(potions, sv)            
            gi = binary_search(potions, sv)            
            # print(f"{i=}, {spell=}, {sv=}, {gi=}, {np - gi}")
            res[i] = np - gi
            
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.successfulPairs([5,1,3], [1,2,3,4,5], 7))  # [4,0,3]
    print(s.successfulPairs([3,1,2], [8,5,8], 16))  # [2,0,2]
            
