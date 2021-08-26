class Solution:
    def reverseWords(self, s: str) -> str:
        return "".join("".join(reversed(word)) + " " for word in s.split()).rstrip()