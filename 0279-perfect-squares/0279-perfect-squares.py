class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp) <= n:
            dp.append(min(dp[-i * i] for i in range(1, int(math.sqrt(len(dp)) + 1))) + 1)
        return dp[n]