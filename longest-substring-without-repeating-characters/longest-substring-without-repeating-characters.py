class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        start = longest = 0
        for i, c in enumerate(s):
            if c in m and start <= m[c]:
                start = m[c] + 1
            else:
                longest = max(longest, i - start + 1)
            m[c] = i
        return longest