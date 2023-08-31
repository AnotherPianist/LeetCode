class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            tap_start, tap_end = max(0, i - ranges[i]), min(n, i + ranges[i])
            
            for j in range(tap_start, tap_end + 1):
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)
            
        return dp[n] if dp[n] != float("inf") else -1