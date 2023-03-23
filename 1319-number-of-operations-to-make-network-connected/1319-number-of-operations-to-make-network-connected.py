class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = [[] for _ in range(n)]
        
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)
        
        connected_components = 0
        visited = [False] * n
        
        for node in range(n):
            if not visited[node]:
                connected_components += 1
                
                stack = [node]
                
                while stack:
                    _node = stack.pop()
                    visited[_node] = True
                    
                    for neighbor in graph[_node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            
        return connected_components - 1
                
                