class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [""] * numRows
        backwards = True
        i = 0
        
        for char in s:
            rows[i] += char
            if i == 0 or i == numRows - 1:
                backwards = not backwards
            i = i - 1 if backwards else i + 1
        
        return "".join(rows)