class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return
    
        def markBorder(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'B'
                markBorder(i + 1, j)
                markBorder(i - 1, j)
                markBorder(i, j + 1)
                markBorder(i, j - 1)

        for i in range(len(board)):
            markBorder(i, 0)
            markBorder(i, len(board[0]) - 1)

        for j in range(len(board[0])):
            markBorder(0, j)
            markBorder(len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'X':
                    board[i][j] = 'X' if board[i][j] is 'O' else 'O'