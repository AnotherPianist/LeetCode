class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bits_to_flip = 0
        
        while a or b or c:
            if c & 1:
                bits_to_flip += 0 if ((a & 1) or (b & 1)) else 1
            else:
                bits_to_flip += (a & 1) + (b & 1)
            
            a, b, c = a >> 1, b >> 1, c >> 1
        
        return bits_to_flip