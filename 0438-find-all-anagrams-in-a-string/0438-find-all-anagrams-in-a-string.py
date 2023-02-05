from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        res = []
        i = 0
        
        for j, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[i]] += 1
                i += 1
            if j - i + 1 == len(p):
                res.append(i)

        return res