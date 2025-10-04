from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        best = min(height[l], height[r]) * (r - l)

        while abs(r - l) > 1:
            print(l, r)
            if height[l] >= height[r]:
                nr = r - 1
                while height[r] >= height[nr]:
                    if nr <= l + 1:
                        r = nr
                        best = max(best, min(height[l], height[r]) * (r - l))
                        return best
                    nr -= 1
                r = nr
            else:
                nl = l + 1
                while height[l] >= height[nl]:
                    if nl >= r + 1:
                        l = nl
                        best = max(best, min(height[l], height[r]) * (r - l))
                        return best
                    nl += 1
                l = nl
            best = max(best, min(height[l], height[r]) * (r - l))

        return best


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]), 49, '\n')
    print()
    print(s.maxArea(height=[8, 7, 2, 1]), 7)
    print()
    print(s.maxArea([1,0,0,0,0,0,0,2,2]), 8)
