class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        order = {char: i for i, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                elif order[words[i][j]] > order[words[i + 1][j]]:
                    return False
                elif order[words[i][j]] < order[words[i + 1][j]]:
                    break
        
        return True