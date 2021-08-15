from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        m = Counter(t)
        required_size = len(m)
        i = j = formed = 0
        min_size, min_i, min_j = float("inf"), 0, 0
        current = defaultdict(int)
        while j < len(s):
            current[s[j]] += 1
            if s[j] in m and current[s[j]] == m[s[j]]:
                formed += 1
            while i <= j and formed == required_size:
                if j - i + 1 < min_size:
                    min_size = j - i + 1
                    min_i, min_j = i, j
                current[s[i]] -= 1
                if s[i] in m and current[s[i]] < m[s[i]]:
                    formed -= 1
                i += 1
            j += 1
        return s[min_i : min_j + 1] if min_size != float("inf") else ""