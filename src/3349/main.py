from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # O(n^2) maybe can do smarter
        N = len(nums)
        inc = 1
        OC = False if k > 1 else True
        for i in range(1, N):
            print(
                f"i={i}, nums[i]={nums[i]}, nums[i-1]={nums[i - 1]}, inc={inc}, OC={OC}"
            )
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                if inc >= k:
                    OC = True
                else:
                    OC = False
                inc = 1
            if inc == 2 * k or (inc == k and OC):
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.hasIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
    print(s.hasIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
    print(s.hasIncreasingSubarrays(nums=[19, 5], k=1))
