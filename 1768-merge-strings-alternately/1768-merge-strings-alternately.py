class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j = 0
        res = ""
        
        for i in range(len(word1)):
            res += word1[i]
            if j < len(word2):
                res += word2[j]
                j += 1
        
        if j < len(word2):
            res += word2[j:]
            
        return res