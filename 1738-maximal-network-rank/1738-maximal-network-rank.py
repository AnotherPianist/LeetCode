from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_rank = 0
        adj = defaultdict(set)

        for src, dst in roads:
            adj[src].add(dst)
            adj[dst].add(src)
        
        for node_1 in range(n):
            for node_2 in range(node_1 + 1, n):
                rank = len(adj[node_1]) + len(adj[node_2])
                
                if node_2 in adj[node_1]:
                    rank -= 1
                
                max_rank = max(max_rank, rank)
        
        return max_rank