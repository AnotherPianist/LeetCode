from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rs, ds = deque(), deque()
        
        for i, c in enumerate(senate):
            if c == 'R':
                rs.append(i)
            else:
                ds.append(i)
        
        while rs and ds:
            r = rs.popleft()
            d = ds.popleft()
            
            if r < d:
                rs.append(r + n)
            else:
                ds.append(d + n)
        
        return "Radiant" if rs else "Dire"