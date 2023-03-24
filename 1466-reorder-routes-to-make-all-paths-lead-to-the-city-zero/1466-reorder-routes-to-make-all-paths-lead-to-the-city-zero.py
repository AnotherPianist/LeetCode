class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for src, dst in connections:
            graph[src].append((dst, 1))
            graph[dst].append((src, 0))
        
        to_reverse = 0
        stack = [(0, 0)]
        visited = set([0])
        
        while stack:
            node, direction = stack.pop()
            
            to_reverse += direction
            
            for neighbor in graph[node]:
                if neighbor[0] not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor[0])
        
        return to_reverse