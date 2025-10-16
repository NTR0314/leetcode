from typing import List
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nc = Counter([num % value for num in nums])
        res = 0
        
        while True:
            mod = res % value
            if nc[mod] > 0:
                nc[mod] -= 1
                res += 1
            else:
                return res


if __name__ == "__main__":
    s = Solution()
    print(s.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5), 4)
    print(s.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7), 2)
    print(s.findSmallestInteger([3,2,3,1,0,1,4,2,3,1,4,1,3], 5), 5)