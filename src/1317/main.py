from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        return self.brute_force(n)

    
    def brute_force(self, n: int) -> List[int]:
        for x in reversed(range(1, n)):
            y = n - x
            if '0' not in str(x) and '0' not in str(y):
                return [x, y]

        return [-1, -1]
        