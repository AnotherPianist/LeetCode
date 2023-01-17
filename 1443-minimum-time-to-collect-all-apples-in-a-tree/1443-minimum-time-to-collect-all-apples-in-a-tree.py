from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        
        for s, d in edges:
            tree[s].append(d)
            tree[d].append(s)
        
        def dfs(node, parent):
            res = 0
            
            for neighbor in tree[node]:
                if neighbor != parent:
                    res += dfs(neighbor, node)
            
            return (res + 2) if (res or hasApple[node]) else res
        
        return max(dfs(0, -1) - 2, 0)