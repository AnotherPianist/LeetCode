class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        r = ""
        for c in b:
            r += '1' if c == '0' else '0'
        return int(r, 2)