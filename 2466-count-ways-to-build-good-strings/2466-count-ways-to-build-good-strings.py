class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        
        for j in range(1, high + 1):
            if j >= zero:
                dp[j] += dp[j - zero]
            if j >= one:
                dp[j] += dp[j - one]
            
            dp[j] %= 1000000007
        
        return sum(dp[low:high + 1]) % 1000000007
        