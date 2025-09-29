class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        neg = False
        aa = numerator < 0
        bb = denominator < 0
        if aa:
            if not bb:
                numerator = -numerator
                neg = True
        elif bb:
            if not aa:
                denominator = - denominator
                neg = True

        res = []
        seen = {}
        n = numerator
        m = denominator
        i = 0
        
        while True:
            if (n, m) in seen:
                add = 1
                if (n, m) == (numerator, denominator):
                    add += 1
                    res = "".join(res[:seen[(n, m)] + add]) + "(" + "".join(res[seen[(n, m)] + add:]) + res[0] + ")"
                else:
                    res = "".join(res[:seen[(n, m)] + add]) + "(" + "".join(res[seen[(n, m)] + add:]) + ")"
                if neg:
                    res = "-" + res
                return res
            else:
                floor = n // m
                res.append(str(floor))
                seen[(n,m)] = i
                rest = n % m
                if rest == 0:
                    break
                if i == 0:
                    res.append(".")
                n = rest * 10
                i += 1
        
        res = "".join(res)
        if neg:
            res = "-" + res
        return res       
        
if __name__ == "__main__":
    s = Solution()
    print(s.fractionToDecimal(420, 226))