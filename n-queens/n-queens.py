class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []
        columns = set()
        positive_diagonals = set()
        negative_diagonals = set()

        def backtracking(i):
            if i == n:
                result.append([''.join(row) for row in board])
                return
            for j in range(n):
                if j not in columns and i + j not in positive_diagonals and i - j not in negative_diagonals:
                    columns.add(j)
                    positive_diagonals.add(i + j)
                    negative_diagonals.add(i - j)
                    board[i][j] = 'Q'

                    backtracking(i + 1)

                    columns.remove(j)
                    positive_diagonals.remove(i + j)
                    negative_diagonals.remove(i - j)
                    board[i][j] = '.'
        
        backtracking(0)
        return result