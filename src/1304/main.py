from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        odd = n % 2 == 0
        
        if odd:
            return [i for i in range(-n // 2, n // 2)]
        else:
            return [i for i in range(-n // 2, n // 2) if i != 0]
        