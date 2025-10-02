class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] + [0] * (n + 1)
        
        for i in range(n):
            dp[i+1] += dp[i]
            dp[i+2] += dp[i]
            
        # print(dp)

        return dp[n]
    
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs(2))
    print(s.climbStairs(4))
