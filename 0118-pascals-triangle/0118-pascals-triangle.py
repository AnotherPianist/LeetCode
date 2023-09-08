class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1]

            if i >= 2:
                for j in range(1, i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            if i >= 1:
                row.append(1)

            triangle.append(row)
        
        return triangle