class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, stack = [], [[0]]
        
        while stack:
            path = stack.pop()
            if path[-1] == len(graph) - 1:
                paths.append(path)
            for neighbor in graph[path[-1]]:
                stack.append(path + [neighbor])
        
        return paths