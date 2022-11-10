class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_sum = 0
            while n > 0:
                total_sum += (n % 10) ** 2
                n //= 10
            return total_sum
        
        slow, fast = n, get_next(n)
        while fast != 1 and fast != slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return slow == 1 or fast == 1