class Solution:
    def toLowerCase(self, s: str) -> str:
        diff = ord('a') - ord('A')
        res = []
        
        for c in s:
            if ord('A') <= ord(c) <= ord('Z'):
                res.append(chr(ord(c) + diff))
            else:
                res.append(c)
                
        return "".join(res)