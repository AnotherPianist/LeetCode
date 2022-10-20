class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        res = 0
        last_val = 0
        
        for c in reversed(s):
            res += values[c] if values[c] >= last_val else -values[c]
            last_val = values[c]

        return res