from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        neighbors = defaultdict(set)
        
        for c1, c2 in zip(s1, s2):
            neighbors[c1].add(c2)
            neighbors[c2].add(c1)
                
        def dfs(c, min_c, visited):
            visited.add(c)
            res = min_c
            
            for neighbor in neighbors[c]:
                if neighbor not in visited:
                    res = min(res, dfs(neighbor, min(min_c, neighbor), visited))
            return res
        
        return "".join([dfs(c, c, set()) for c in baseStr])