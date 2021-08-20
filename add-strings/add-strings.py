class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        val1 = val2 = 0
        for i, c in enumerate(reversed(num1)):
            val1 += int(c) * (10 ** i)
        for i, c in enumerate(reversed(num2)):
            val2 += int(c) * (10 ** i)
        return str(val1 + val2)