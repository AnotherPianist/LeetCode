from collections import defaultdict


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        def rabinKarp(m, q):
            if m == 0:
                return True
            h, t, d = (1 << (8 * m - 8)) % q, 0, 256
            dic = defaultdict(list)
            for i in range(m): 
                t = (d * t + ord(s[i])) % q
            dic[t].append(i - m + 1)
            for i in range(len(s) - m):
                t = (d * (t - ord(s[i]) * h) + ord(s[i + m])) % q
                for j in dic[t]:
                    if s[i + 1:i + m + 1] == s[j:j + m]:
                        return (True, s[j:j + m])
                dic[t].append(i + 1)
            return (False, "")
        
        left, right = 0, len(s)
        q = (1<<31) - 1
        found = ""
        while left + 1 < right:
            mid = (left + right) // 2
            isFound, candidate = rabinKarp(mid, q)
            if isFound:
                left, found = mid, candidate
            else:
                right = mid
        return found