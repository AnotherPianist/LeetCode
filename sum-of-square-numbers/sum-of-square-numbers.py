class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            if math.sqrt(c - a * a).is_integer():
                return True
            a += 1
        return False