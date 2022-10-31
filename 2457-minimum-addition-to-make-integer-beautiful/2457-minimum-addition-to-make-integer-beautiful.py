from math import ceil

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        m = n
        power = 10
        
        while sum(map(int, str(m))) > target:
            m = ceil(m / power) * power
            power *= 10
        
        return m - n