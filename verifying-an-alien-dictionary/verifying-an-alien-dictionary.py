class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        values = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]):
                if j >= len(words[i + 1]):
                    return False
                if values[words[i][j]] < values[words[i + 1][j]]:
                    break
                elif values[words[i][j]] == values[words[i + 1][j]]:
                    j += 1
                else:
                    return False
        return True