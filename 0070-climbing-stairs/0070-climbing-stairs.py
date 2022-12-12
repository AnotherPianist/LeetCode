class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1: 1, 2: 2}
        
        def recursion(num):
            if num in dp:
                return dp[num]
            dp[num] = recursion(num - 1) + recursion(num - 2)
            return dp[num]
        
        return recursion(n)