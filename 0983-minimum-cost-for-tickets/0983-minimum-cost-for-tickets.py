class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        dp = [0] * (days[-1] + 1)
        
        for i in range(days[-1] + 1):
            if i not in days_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                
        return dp[-1]