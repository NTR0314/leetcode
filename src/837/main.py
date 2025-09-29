class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        sliding_window = 1
        for i in range(1, n + 1):
            dp[i] = sliding_window / maxPts
            if i < k:
                sliding_window = sliding_window + dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                sliding_window = sliding_window - dp[i - 1 - maxPts]

        return sum(dp[k:])

if __name__ == "__main__":
    solution = Solution()
    new21Game = solution.new21Game
    n = 21
    k = 17
    maxPts = 10
    print(f"The probability is: {new21Game(n, k, maxPts)}") # Output: 0.73278