from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m, n = len(mat), len(mat[0])
        matrix = [row[:] for row in mat]
        queue = deque()
        seen = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))
                    seen.add((i, j))
        
        while queue:
            i, j, steps = queue.pop()

            for next_i, next_j in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                if (next_i, next_j) not in seen and valid(next_i, next_j):
                    seen.add((next_i, next_j))
                    queue.appendleft((next_i, next_j, steps + 1))
                    matrix[next_i][next_j] = steps + 1
            
        return matrix