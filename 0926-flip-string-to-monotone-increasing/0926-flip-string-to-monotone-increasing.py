class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = 0
        
        for c in s:
            if c == '0':
                count += 1

        res = count

        for c in s:
            if c == '0':
                count -= 1
                res = min(res, count)
            else:
                count += 1
        
        return res