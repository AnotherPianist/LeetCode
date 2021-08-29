from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        startTime = [job[0] for job in jobs]
        dp = [0] * (len(jobs) + 1)
        for i in range(len(jobs) - 1, -1, -1):
            dp[i] = max(jobs[i][2] + dp[bisect_left(startTime, jobs[i][1])], dp[i + 1])
        return dp[0]