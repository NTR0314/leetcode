from typing import List


class Solution:
    def gcd(self, a, b):
        if a >= b:
            bigger = a
            smaller = b
        else:
            smaller = a
            bigger = b
        
        mod_resid = bigger % smaller

        if mod_resid == 0:
            return smaller
        else:
            return self.gcd(smaller, mod_resid)

    def lcm(self, a, b, gcd):
        # https://en.wikipedia.org/wiki/Least_common_multiple
        return int(abs(a * b) / gcd)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            while res and (gcd_calc := self.gcd(res[-1], n)) > 1:
                n = self.lcm(res.pop(), n, gcd_calc)

            res.append(n)
        
        return res
        