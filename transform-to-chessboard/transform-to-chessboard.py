class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(len(board)) for j in range(len(board))): return -1
        if not len(board) // 2 <= sum(board[0]) <= (len(board) + 1) // 2:
            return -1
        if not len(board) // 2 <= sum(board[i][0] for i in range(len(board))) <= (len(board) + 1) // 2:
            return -1
        col = sum(board[0][i] == i % 2 for i in range(len(board)))
        row = sum(board[i][0] == i % 2 for i in range(len(board)))
        if len(board) % 2:
            if col % 2:
                col = len(board) - col
            if row % 2:
                row = len(board) - row
        else:
            col = min(len(board) - col, col)
            row = min(len(board) - row, row)
        return (col + row) // 2