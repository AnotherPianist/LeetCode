class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        q = deque()
        coordinates = ((-1, 0), (0, 1), (1, 0), (0, -1))
        time = 0
        fresh_count = 0

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    q.append((i, j))
                elif val == 1:
                    fresh_count += 1

        while q and fresh_count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in coordinates:
                    adj_i, adj_j = i + x, j + y
                    if adj_i < 0 or adj_i == len(grid) or adj_j < 0 or adj_j == len(grid[0]) or grid[adj_i][adj_j] == 0 or grid[adj_i][adj_j] == 2:
                        continue
                    grid[adj_i][adj_j] = 2
                    q.append((adj_i, adj_j))
                    fresh_count -= 1
            time += 1

        if fresh_count > 0:
            return -1
        return time