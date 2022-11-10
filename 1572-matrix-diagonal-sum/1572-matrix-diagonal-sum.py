class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        
        if size == 1:
            return mat[0][0]
        
        sum = 0
        
        for i in range(size):
            sum += mat[i][i] + mat[i][size - i - 1]
            
        if size % 2 == 1:
            sum -= mat[size // 2][size // 2]

        return sum