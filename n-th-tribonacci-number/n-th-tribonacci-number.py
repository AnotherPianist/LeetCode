class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1
        t0, t1, t2 = 0, 1, 1
        i = 2
        while i < n:
            t0, t1, t2 = t1, t2, t0 + t1 + t2
            i += 1
        return t2