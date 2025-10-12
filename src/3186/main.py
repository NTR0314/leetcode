from typing import List


# TODO finish
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Helper function that calculates tuples (damage, count) 
        # into a sorted list.
        def helper(power: List[int]) -> List[tuple[int, int]]:
            power.sort()
            result = []
            count = 1
            for i in range(1, len(power)):
                if power[i] == power[i - 1]:
                    count += 1
                else:
                    result.append((power[i - 1], count))
                    count = 1
            result.append((power[-1], count))
            return result
        
        power_tuples = helper(power)
        
        res = [0] * len(power_tuples)
        # init
        res[0] = power_tuples[0][0] * power_tuples[0][1]
        for i in range(1, len(power_tuples)):
            if abs(power_tuples[i][0] - power_tuples[i - 1][0]) > 2:
                res[i] = max(res[i], res[i - 1] + power_tuples[i][0] * power_tuples[i][1])
            else:
                if i >= 2:
                    res[i] = max(res[i], res[i - 2] + power_tuples[i][0] * power_tuples[i][1])
                else:
                    res[i] = max(res[i], power_tuples[i][0] * power_tuples[i][1])


        
if __name__ == "__main__":
    s = Solution()
    print(s.maximumTotalDamage(power = [1,1,3,4]), 6)
    print(s.maximumTotalDamage(power = [7,1,6,6]), 13)