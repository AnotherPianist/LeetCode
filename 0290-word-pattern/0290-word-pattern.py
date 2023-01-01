class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        m = {}
        
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False
        
        for c, word in zip(pattern, s):
            if word not in m:
                m[word] = c
            elif m[word] != c:
                return False
            
        return True