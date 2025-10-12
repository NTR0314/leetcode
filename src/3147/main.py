from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # init
        poss = energy[:k]
        for s in range(k, len(energy)):
            ci = s % k
            poss[ci] = max(poss[ci] + energy[s], energy[s])

        return max(poss)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumEnergy(energy=[5, 2, -10, -5, 1], k=3))
    print(s.maximumEnergy([-2, -3, -1], k=2))
