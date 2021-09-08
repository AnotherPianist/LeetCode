class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts) % 26
        res = []
        for i, c in enumerate(s):
            res.append(chr(ord('a') + (ord(c) - ord('a') + total) % 26))
            total = (total - shifts[i]) % 26
        return "".join(res)