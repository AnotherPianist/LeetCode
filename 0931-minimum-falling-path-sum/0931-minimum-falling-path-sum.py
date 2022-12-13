class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j <= 0:
                    min_val = min(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j >= len(matrix[0]) - 1:
                    min_val = min(matrix[i - 1][j - 1], matrix[i - 1][j])
                else:
                    min_val = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])
                matrix[i][j] += min_val
        return min(matrix[-1])