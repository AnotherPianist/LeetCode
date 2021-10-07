class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) * len(board[0]) < len(word):
            return False
        visited = set()
        
        def backtrack(s, i, j):
            s += board[i][j]
            if s == word:
                return True
            elif len(s) > len(word):
                return False
            
            visited.add((i, j))
            found = False
            if s == word[:len(s)]:
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ii, jj = i + di, j + dj
                    if (ii, jj) not in visited and 0 <= ii < len(board) and 0 <= jj < len(board[0]):
                        found = backtrack(s, ii, jj)
                        if found:
                            return True
                        visited.remove((ii, jj)) 
            return found
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == word[0]:
                    visited.clear()
                    if backtrack("", i, j):
                        return True
        return False