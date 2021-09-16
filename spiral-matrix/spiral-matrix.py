class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i_start = j_start = 0
        i_end, j_end = len(matrix) - 1, len(matrix[0]) - 1
        res = []
        while i_start <= i_end and j_start <= j_end:
            for j in range(j_start, j_end + 1):
                res.append(matrix[i_start][j])
            i_start += 1
            for i in range(i_start, i_end + 1):
                res.append(matrix[i][j_end])
            j_end -= 1
            if i_end >= i_start:
                for j in range(j_end, j_start - 1, -1):
                    res.append(matrix[i_end][j])
                i_end -= 1
            if j_start <= j_end:
                for i in range(i_end, i_start - 1, -1):
                    res.append(matrix[i][j_start])
                j_start += 1
        return res