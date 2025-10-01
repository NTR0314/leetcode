from typing import List
import math


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def binom(n, k):
            # return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
            return math.comb(n, k)
            
        n = len(nums)
        res = 0
        for k, num in enumerate(nums, start=0):
            binom_param = binom(n - 1, k)
            # print(n, k, binom_param, num)
            res += binom_param * num

        return res % 10

            
if __name__ == "__main__":
    s = Solution()
    print('\n', s.triangularSum([1,2,3,4,5]))
    print('\n', s.triangularSum([5]))