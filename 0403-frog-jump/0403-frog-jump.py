class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        if len(stones) == 2 and stones[0] == 0 and stones[1] == 1:
            return True
        
        dp = {}
        for stone in stones:
            dp[stone] = set()
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k - 1)
                if stone + k in dp:
                    dp[stone + k].add(k)
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)

        return len(dp[stones[-1]]) > 0
