class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        in_degree = [0] * len(colors)
        graph = [[] for _ in range(len(colors))]
        
        for src, dst in edges:
            in_degree[dst] += 1
            graph[src].append(dst)
        
        stack = [node for node in range(len(colors)) if in_degree[node] == 0]
        counts = [[0] * 26 for _ in range(len(colors))]
        
        while stack:
            node = stack.pop()
            counts[node][ord(colors[node]) - ord('a')] += 1
            
            for neighbor in graph[node]:
                counts[neighbor] = list(map(max, counts[neighbor], counts[node]))
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
        
        return -1 if sum(in_degree) > 0 else max([max(node) for node in counts])