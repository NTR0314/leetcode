class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a_even = n // 2 
        a_uneven = (n + 1) // 2
        b_even = m // 2 
        b_uneven = (m + 1) // 2

        return a_even * b_uneven + b_even * a_uneven