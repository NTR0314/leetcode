class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        e = numBottles
        while (r := (e // numExchange)) >= 1:
            print(res, e, r)
            res += r
            e = (e % numExchange) + r
            
        return res

        
        
if __name__ == "__main__":
    s = Solution()
    assert s.numWaterBottles(numBottles = 9, numExchange = 3) == 13
    print()
    assert s.numWaterBottles(numBottles = 15, numExchange = 4) == 19