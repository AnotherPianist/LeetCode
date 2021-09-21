class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[-1] * 3 for _ in range(3)]
        
        diagonals = (((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
        combinations = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)))
        
        for i, move in enumerate(moves):
            board[move[0]][move[1]] = i % 2
            
        for diag in diagonals:
            if board[diag[0][0]][diag[0][1]] != -1 and board[diag[0][0]][diag[0][1]] == board[diag[1][0]][diag[1][1]] == board[diag[2][0]][diag[2][1]]:
                return "A" if board[diag[0][0]][diag[0][1]] == 0 else "B"
            
        for comb in combinations:
            if board[comb[0][0]][comb[0][1]] != -1 and board[comb[0][0]][comb[0][1]] == board[comb[1][0]][comb[1][1]] == board[comb[2][0]][comb[2][1]]:
                return "A" if board[comb[0][0]][comb[0][1]] == 0 else "B"
            elif board[comb[0][1]][comb[0][0]] != -1 and board[comb[0][1]][comb[0][0]] == board[comb[1][1]][comb[1][0]] == board[comb[2][1]][comb[2][0]]:
                return "A" if board[comb[0][1]][comb[0][0]] == 0 else "B"
        
        return "Draw" if len(moves) == 9 else "Pending"