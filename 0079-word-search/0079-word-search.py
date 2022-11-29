class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) * len(board[0]) < len(word):
            return False

        def backtrack(s, i, j):
            s += board[i][j]
            visited.add((i, j))
            if s == word:
                return True
            if len(s) > len(word):
                return False
            found = False
            if s == word[:len(s)]:
                if (i - 1, j) not in visited and i > 0:
                    found = backtrack(s, i - 1, j)
                    visited.remove((i - 1, j))
                if not found and (i, j + 1) not in visited and j + 1 <= len(board[0]) - 1:
                    found = backtrack(s, i, j + 1)
                    visited.remove((i, j + 1))
                if not found and (i + 1, j) not in visited and i + 1 <= len(board) - 1:
                    found = backtrack(s, i + 1, j)
                    visited.remove((i + 1, j))
                if not found and (i, j - 1) not in visited and j > 0:
                    found = backtrack(s, i, j - 1)
                    visited.remove((i, j - 1))
            return found

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    visited = set()
                    if backtrack("", i, j):
                        return True
        return False