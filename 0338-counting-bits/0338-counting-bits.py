class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            x = i

            while x != 0:
                x &= x - 1
                count += 1

            res.append(count)
    
        return res