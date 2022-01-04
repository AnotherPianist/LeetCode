class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        r = ""
        for c in b:
            r += '1' if c == '0' else '0'
        return int(r, 2)