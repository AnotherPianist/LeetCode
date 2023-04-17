class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        k = len(words[0])
        count = [[0] * k for _ in range(26)]
        
        for j in range(k):
            for word in words:
                count[ord(word[j]) - ord('a')][j] += 1
        
        dp = [[0] * (k + 1) for _ in range(len(target) + 1)]
        dp[0][0] = 1
        
        for i in range(len(target) + 1):
            for j in range(k):
                if i < len(target):
                    dp[i + 1][j + 1] += count[ord(target[i]) - ord('a')][j] * dp[i][j]
                    dp[i + 1][j + 1] %= 1000000007
                
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= 1000000007
        
        return dp[len(target)][k]