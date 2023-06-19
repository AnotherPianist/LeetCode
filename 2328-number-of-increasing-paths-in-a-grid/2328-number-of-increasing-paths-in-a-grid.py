class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mod = int(1e9 + 7)
        
        dp = [[0] * m for _ in range(n)]
        
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            
            path_len = 1
            
            for next_i, next_j in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] > grid[i][j]:
                    path_len += dfs(next_i, next_j) % mod
            
            dp[i][j] = path_len
            return path_len
        
        return sum(dfs(i, j) for i in range(n) for j in range(m)) % mod
            