from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(f"nums={nums}")
        res = set()

        a = defaultdict(lambda: 0)
        for num in nums:
            a[num] += 1

        nums.sort()
        
        done = set()

        # Fix third number
        for i, t in enumerate(nums):
            if t in done:
                continue
            # Two pointer
            r = len(nums) - 1
            l = i + 1
            while l < r:
                # print(f"t={t}, l={l}, r={r}, nums[l]={nums[l]}, nums[r]={nums[r]}")
                if (z := (nums[l] + nums[r] + t)) == 0:
                    if tuple(sorted((t, nums[l], nums[r]))) not in res:
                        res.add(tuple(sorted((t, nums[l], nums[r]))))
                    l += 1
                elif z > 0:
                    r -= 1
                else:
                    l += 1
            done.add(t)
                

        return list([list(x) for x in res])


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(s.threeSum(nums=[0, 1, 1]))
    print(s.threeSum(nums=[0, 0, 0]))
    print(s.threeSum(nums=[-100, -70, -60, 110, 120, 130, 160]))
