class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        matches = [1] + [0] * len(t)
        for i in range(len(s)):
            for j in range(len(t) - 1, -1, -1):
                if t[j] == s[i]:
                    matches[j + 1] += matches[j]
        return matches[-1]