class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n = len(s), len(str(k))
        dp = [1] + [0] * n
        
        for start in range(m):
            if s[start] == '0':
                dp[start % (n + 1)] = 0
                continue
            
            for end in range(start, m):
                if int(s[start : end + 1]) > k:
                    break
                
                dp[(end + 1) % (n + 1)] += dp[start % (n + 1)]
                dp[(end + 1) % (n + 1)] %= 1000000007
            
            dp[start % (n + 1)] = 0
        
        return dp[m % (n + 1)]