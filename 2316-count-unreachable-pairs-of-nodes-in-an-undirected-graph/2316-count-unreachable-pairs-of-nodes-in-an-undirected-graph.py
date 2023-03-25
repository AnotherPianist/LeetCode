class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        visited = set()
        
        def count(node):
            if node in visited:
                return 0
            visited.add(node)
            return sum(count(neighbor) for neighbor in graph[node]) + 1
        
        return sum((size := count(i)) * (n - size) for i in range(n) if i not in visited) // 2