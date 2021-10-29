from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        q = deque()
        time = fresh_count = 0

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    q.append((i, j))
                elif val == 1:
                    fresh_count += 1

        while q and fresh_count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    adj_i, adj_j = i + x, j + y
                    if 0 <= adj_i < len(grid) and 0 <= adj_j < len(grid[0]) and grid[adj_i][adj_j] == 1:
                        grid[adj_i][adj_j] = 2
                        q.append((adj_i, adj_j))
                        fresh_count -= 1
            time += 1

        if fresh_count > 0:
            return -1
        return time