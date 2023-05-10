class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        
        num = 0
        i_start = j_start = 0
        i_end = j_end = n
        
        while num < n ** 2:
            for j in range(j_start, j_end):
                num += 1
                matrix[i_start][j] = num
            i_start += 1
            
            for i in range(i_start, i_end):
                num += 1
                matrix[i][j_end - 1] = num
            j_end -= 1
            
            for j in range(j_end - 1, j_start - 1, -1):
                num += 1
                matrix[i_end - 1][j] = num
            i_end -= 1
            
            for i in range(i_end - 1, i_start - 1, -1):
                num += 1
                matrix[i][j_start] = num
            j_start += 1
        
        return matrix