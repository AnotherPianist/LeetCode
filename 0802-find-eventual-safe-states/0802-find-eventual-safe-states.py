from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph = defaultdict(list)
        dp = [0] * n
        
        for i, nodes in enumerate(graph):
            dp[i] = len(nodes)
            
            for node in nodes:
                reversed_graph[node].append(i)
        
        stack = [i for i in range(n) if dp[i] == 0]
        
        while stack:
            node = stack.pop()
            
            for neighbor in reversed_graph[node]:
                dp[neighbor] -= 1
                
                if dp[neighbor] == 0:
                    stack.append(neighbor)
        
        return [i for i in range(n) if dp[i] == 0]