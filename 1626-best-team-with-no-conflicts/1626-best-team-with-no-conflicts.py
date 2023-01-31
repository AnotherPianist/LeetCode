class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        data = sorted(zip(ages, scores))
        dp = [0] * len(data)
        res = 0
        
        for i in range(len(data)):
            dp[i] = data[i][1]
            for j in range(i):
                if data[j][1] <= data[i][1]:
                    dp[i] = max(dp[i], dp[j] + data[i][1])
            res = max(res, dp[i])

        return res