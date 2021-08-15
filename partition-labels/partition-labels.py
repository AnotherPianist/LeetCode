class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i, c in enumerate(s):
            m[c] = i
        
        j = prev = 0
        res = [0]
        for i, c in enumerate(s):
            j = max(j, m[c])
            if i == j:
                res.append(j - prev + 1)
                prev = j + 1
        return res[1:]