from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            i = 0
            j = len(nums) - 1
            res = set()
            while i < j:
                s = nums[i] + nums[j]
                if s < target:
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    res.add(tuple(sorted([nums[i], nums[j]])))
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
            return res
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                two_sum_res = twoSum(nums[j + 1:], target - nums[i] - nums[j])
                for pair in two_sum_res:
                    res.add(tuple(sorted([nums[i], nums[j]] + [pair[0], pair[1]])))
        return [list(item) for item in res]
            

if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([2, 2, 2, 2, 2], 8))