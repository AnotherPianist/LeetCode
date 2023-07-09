from collections import Counter
from itertools import product


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        chars = set(s)
        res = 0
        
        for a, b in product(chars, chars):
            if a == b:
                continue
            a_count = b_count = 0
            remaining_b = counter[b]
            
            for c in s:
                if c == a:
                    a_count += 1
                elif c == b:
                    b_count += 1
                    remaining_b -= 1
                
                if b_count:
                    res = max(res, a_count - b_count)
                if a_count < b_count and remaining_b > 0:
                    a_count = b_count = 0
        
        return res