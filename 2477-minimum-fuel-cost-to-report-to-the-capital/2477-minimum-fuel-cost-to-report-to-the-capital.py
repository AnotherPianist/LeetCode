from math import ceil


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for _ in range(len(roads) + 1)]
        
        for src, dst in roads:
            graph[src].append(dst)
            graph[dst].append(src)
        
        fuel = 0

        def dfs(node, parent):
            nonlocal fuel
            representatives = 1
            
            for child in graph[node]:
                if child != parent:
                    representatives += dfs(child, node)
            
            if node != 0:
                fuel += ceil(representatives / seats)
            
            return representatives


        dfs(0, -1)
        
        return fuel