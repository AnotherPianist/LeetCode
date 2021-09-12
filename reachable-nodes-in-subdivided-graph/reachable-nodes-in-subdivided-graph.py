from collections import defaultdict

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
            
        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        res = 0
        
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            res += 1
            for nei, weight in graph[node].items():
                v = min(weight, maxMoves - d)
                used[node, nei] = v
                d2 = d + weight + 1
                if d2 < dist.get(nei, maxMoves + 1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2
        
        for u, v, w in edges:
            res += min(w, used.get((u, v), 0) + used.get((v, u), 0))
        return res