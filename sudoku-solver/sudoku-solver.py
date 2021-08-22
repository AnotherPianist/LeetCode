class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell != '.':
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[3 * (r // 3) + (c // 3)].add(cell)
                    
        def backtracking(r, c):
            if c == 9:
                r += 1
                c = 0
            if r == 9:
                return True
            if board[r][c] != '.':
                return backtracking(r, c + 1)
            for val in range(1, 10):
                val = str(val)
                if val not in rows[r] and val not in cols[c] and val not in boxes[3 * (r // 3) + (c // 3)]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[3 * (r // 3) + (c // 3)].add(val)
                    
                    if backtracking(r, c + 1):
                        return True
                    
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[3 * (r // 3) + (c // 3)].remove(val)
                    
        backtracking(0, 0)