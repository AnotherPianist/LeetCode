class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i != 0 and j != 0 and matrix[i - 1][j - 1] != val:
                    return False
        return True