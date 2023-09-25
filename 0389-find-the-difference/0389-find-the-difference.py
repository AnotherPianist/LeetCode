class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xors = 0

        for char in s:
            xors ^= ord(char) - ord('a')
        for char in t:
            xors ^= ord(char) - ord('a')
        
        return chr(xors + ord('a'))