class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        
        for word in words:
            dp = [False] * (len(word) + 1)
            dp[0] = True
            
            for i in range(1, len(word) + 1):
                for j in range((i == len(word)), i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in words
            
            if dp[len(word)]:
                res.append(word)
            
        return res