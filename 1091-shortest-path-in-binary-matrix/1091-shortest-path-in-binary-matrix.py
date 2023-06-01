from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if n == 1:
            return 1 if grid[0][0] == 0 else -1
        elif grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        path_length = 1
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                directions = ((i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1))

                for next_i, next_j in directions:
                    if 0 <= next_i < n and 0 <= next_j < n and (next_i, next_j) not in visited:
                        if next_i == n - 1 and next_j == n - 1:
                            return path_length + 1
                        elif grid[next_i][next_j] == 0:
                            queue.append((next_i, next_j))
                            visited.add((next_i, next_j))

                
            path_length += 1
        
        return -1