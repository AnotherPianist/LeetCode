class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = set(tuple(mine) for mine in mines)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > res:
                    res = dp[r][c]
        return res