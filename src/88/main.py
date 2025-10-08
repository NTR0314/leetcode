from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        p1 = m - 1
        p2 = n - 1
        wp = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[wp] = nums2[p2]
                p2 -= 1
                wp -= 1
            else:
                nums1[wp] = nums1[p1]
                p1 -= 1
                wp -= 1

        print(nums1)        
        