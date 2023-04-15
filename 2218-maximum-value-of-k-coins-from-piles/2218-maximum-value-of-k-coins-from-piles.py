class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
        
        for i in range(1, len(piles) + 1):
            for coins in range(k + 1):
                curr_sum = 0
                
                for curr_coins in range(min(len(piles[i - 1]), coins) + 1):
                    if curr_coins > 0:
                        curr_sum += piles[i - 1][curr_coins - 1]
                    
                    dp[i][coins] = max(dp[i][coins], dp[i - 1][coins - curr_coins] + curr_sum)
        
        return dp[len(piles)][k]