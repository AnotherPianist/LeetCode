class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        
        for i in range(1, n + 1):
            res *= i
            res *= 2 * i - 1
            res %= 1_000_000_007
        
        return res