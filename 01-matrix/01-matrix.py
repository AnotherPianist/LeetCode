class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell != 0:
                    top = mat[i - 1][j] if i > 0 else float('inf')
                    left = mat[i][j - 1] if j > 0 else float('inf')
                    mat[i][j] = min(top, left) + 1
        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[0]) - 1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i + 1][j] if i + 1 < len(mat) else float('inf')
                    right = mat[i][j + 1] if j + 1 < len(mat[0]) else float('inf')
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
        return mat