class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = []
        
        def dfs(i, formed):
            if i >= len(s):
                res.append(list(formed))
            
            for j in range(i, len(s)):
                if s[j] == s[i] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    formed.append(s[i:j + 1])
                    dfs(j + 1, formed)
                    formed.pop()
        
        dfs(0, [])
        
        return res