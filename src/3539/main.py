from typing import List
from itertools import combinations_with_replacement as coom
from functools import reduce
from math import factorial as fag
from collections import Counter


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        def check_bits(comb):
            def set_bits(a, new_num):
                if new_num in a and a[new_num]:
                    a[new_num] = False
                    set_bits(a, new_num + 1)
                else:
                    a[new_num] = True

            a = {}
            for num in comb:
                set_bits(a, num)
            aa = [None for x in a.values() if x]
            return len(aa) == k

        res = 0
        a = coom(range(len(nums)), m)

        for comb in a:
            if check_bits(comb):
                counts = [x for x in Counter(comb).values() if x > 1]
                perms = fag(m)
                for count in counts:
                    perms //= fag(count)
                
                num_comb = [nums[i] for i in comb]
                tmp = reduce(lambda x, y: x * y, num_comb) * perms
                # print(f"valid comb: {num_comb}, {perms=}, {tmp=}")
                res += tmp
                res %= 10**9 + 7

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.magicalSum(m=5, k=5, nums=[1, 10, 100, 10000, 1000000]))
    print(s.magicalSum(m=2, k=2, nums=[5, 4, 3, 2, 1]))
    print(s.magicalSum(m=2, k=1, nums=[63]))
    print(s.magicalSum(m=3, k=2, nums=[33]))
    print(s.magicalSum(m=3, k=2, nums=[8, 32]), 57856)
