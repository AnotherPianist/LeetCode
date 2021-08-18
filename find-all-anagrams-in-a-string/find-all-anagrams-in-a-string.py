from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        i = 0
        desired, current = Counter(p), Counter(s[:len(p) - 1])
        res = []
        while i + len(p) - 1 < len(s):
            current[s[i + len(p) - 1]] += 1
            if current == desired:
                res.append(i)
            current[s[i]] = current[s[i]] - 1
            if current[s[i]] <= 0:
                del current[s[i]]
            i += 1
        return res