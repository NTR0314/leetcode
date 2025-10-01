class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        cost = numExchange

        # print(f"{drunk=}, {empty=}")
        while (empty - cost) >= 0:
            drunk += 1
            empty += 1 - cost
            cost += 1
            # print(f"{drunk=}, {empty=}")
            
        # print(drunk)
        return drunk
    
if __name__ == "__main__":
    s = Solution()
    assert s.maxBottlesDrunk(numBottles = 13, numExchange = 6) == 15
    assert s.maxBottlesDrunk(numBottles = 10, numExchange = 3) == 13
