from collections import defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for src, dst in redEdges:
            graph[src].append((dst, 0))
        for src, dst in blueEdges:
            graph[src].append((dst, 1))
        
        visited = set()
        distance = 0
        
        res = [float("inf")] * n
        
        queue = deque([(0, 0), (0, 1)])
        
        while queue:
            for _ in range(len(queue)):
                curr_node, curr_color = queue.popleft()
                res[curr_node] = min(res[curr_node], distance)
                
                for next_node, next_color in graph[curr_node]:
                    if next_color != curr_color and (next_node, next_color) not in visited:
                        queue.append((next_node, next_color))
                        visited.add((next_node, next_color))
            
            distance += 1
        
        for i, val in enumerate(res):
            if val == float("inf"):
                res[i] = -1
        
        return res
                