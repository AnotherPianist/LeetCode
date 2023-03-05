from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        
        graph = defaultdict(list)
        
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        queue = [0]
        visited = {0}
        step = 0
        
        while queue:
            next_vals = []
            
            for node in queue:
                if node == len(arr) - 1:
                    return step
                
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        next_vals.append(child)
                
                graph[arr[node]].clear()
                
                for child in [node - 1, node + 1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        next_vals.append(child)
                        
            queue = next_vals
            step += 1
        
        return -1