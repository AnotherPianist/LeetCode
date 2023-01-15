from collections import defaultdict
from math import comb


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        uf = {}
        
        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
        
        tree = defaultdict(list)
        val2nodes = defaultdict(set)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            val2nodes[vals[u]].add(u)
            val2nodes[vals[v]].add(v)
        
        res = len(vals)
        
        for v in sorted(val2nodes.keys()):
            for node in val2nodes[v]:
                for neighbor in tree[node]:
                    if vals[neighbor] <= v:
                        union(node, neighbor)
                        
            counts = defaultdict(int)
            for node in val2nodes[v]:
                counts[find(node)] += 1
            
            for root in counts.keys():
                res += comb(counts[root], 2)  # count[root] * (count[root] - 1) // 2
        
        return res