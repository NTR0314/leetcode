from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)

        full_lakes = {}
        dry_days = []

        for i, lake in enumerate(rains):
            if lake > 0:
                ans[i] = -1
                if lake not in full_lakes:
                    full_lakes[lake] = i
                else:
                    if not dry_days:
                        return []
                    j = 0
                    while j < len(dry_days) and dry_days[j] < full_lakes[lake]:
                        j += 1
                    if j == len(dry_days):
                        return []
                    ans[dry_days[j]] = lake
                    dry_days.pop(j)
                    full_lakes[lake] = i
            else:
                dry_days.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.avoidFlood(rains = [1,2,3,4]))
    print(s.avoidFlood(rains = [1,2,0,0,2,1]))
    print(s.avoidFlood(rains = [1,2,0,1,2]))
    print(s.avoidFlood([1,2,0,2,3,0,1]))
    print(s.avoidFlood([1,2,0,1,2]))
    print(s.avoidFlood([1,0,2,0]))