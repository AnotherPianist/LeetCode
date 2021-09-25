from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == len(grid[0]) == 1:
            return 0
        q = deque([(0, 0, 0, 0)])
        visited = set()
        while q:
            i, j, obstacles, path_length = q.popleft()
            for ii, jj in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]):
                    if grid[ii][jj] == 1 and obstacles < k and (ii, jj, obstacles + 1) not in visited:
                        visited.add((ii, jj, obstacles + 1))
                        q.append((ii, jj, obstacles + 1, path_length + 1))
                    if grid[ii][jj] == 0 and (ii, jj, obstacles) not in visited:
                        if ii == len(grid) - 1 and jj == len(grid[0]) - 1:
                            return path_length + 1
                        visited.add((ii, jj, obstacles))
                        q.append((ii, jj, obstacles, path_length + 1))
        return -1