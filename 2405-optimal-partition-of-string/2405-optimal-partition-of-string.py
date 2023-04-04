class Solution:
    def partitionString(self, s: str) -> int:
        last_seen = [-1] * 26
        substrings = 1
        last_substring_start = 0
        
        for i, char in enumerate(s):
            if last_seen[ord(char) - ord('a')] >= last_substring_start:
                substrings += 1
                last_substring_start = i
            last_seen[ord(char) - ord('a')] = i
        
        return substrings