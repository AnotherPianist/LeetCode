class Solution:
#    def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         if n < 0:
#             return 1.0 / self.myPow(x, -n)
        
#         return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, (n - 1) // 2)


    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1.0 / x
        
        res = 1
        
        while n != 0:
            if n % 2 == 1:
                res *= x
                n -= 1
            x *= x
            n //= 2
        
        return res