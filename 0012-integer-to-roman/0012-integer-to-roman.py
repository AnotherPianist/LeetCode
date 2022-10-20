class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",  # XD
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        
        res = ""
        
        for n in values:
            while num >= n:
                res += values[n]
                num -= n

        return res