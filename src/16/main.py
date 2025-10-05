from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = sys.maxsize
        res = None
        nums.sort()
        done = set()
        for i, t in enumerate(nums):
            if t in done:
                continue
            r = len(nums) - 1
            l = i + 1
            while l < r:
                cd = (t + nums[l] + nums[r] - target)
                # print(f"t={t}, l={l}, r={r}, nums[l]={nums[l]}, nums[r]={nums[r]}, cd={cd}, best={best}")
                if abs(cd) < best:
                    best = abs(cd)
                    res = t + nums[l] + nums[r]
                if cd >= 0:
                    r -= 1
                else:
                    l += 1
            done.add(t)

        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest(nums =[4,0,5,-5,3,3,0,-4,-5], target = -2))
    print(s.threeSumClosest(nums =[0,0,0], target = 10000))