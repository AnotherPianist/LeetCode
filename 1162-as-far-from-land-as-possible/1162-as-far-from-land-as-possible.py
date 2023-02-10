from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    queue.append((i, j))
        
        if not queue or len(grid) * len(grid[0]) == len(queue):
            return -1
        
        visited = set()
        distance = 0
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        
        while queue:
            for _ in range(len(queue)):
                curr_i, curr_j = queue.popleft()
                
                for _i, _j in directions:
                    next_i, next_j = curr_i + _i, curr_j + _j
                    
                    if len(grid) > next_i >= 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == 0 and (next_i, next_j) not in visited:
                        queue.append((next_i, next_j))
                        visited.add((next_i, next_j))
                
            distance += 1
        
        return distance - 1