from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.isEnd = False
        
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.links[c]
        node.isEnd = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        
        def dfs(i, j, formed, node):
            if node.isEnd:
                res.append(formed)
                node.isEnd = False
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                c = board[i][j]
                node = node.links.get(c)
                if node:
                    board[i][j] = '.'
                    for ii, jj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        dfs(i + ii, j + jj, formed + c, node)
                    board[i][j] = c
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", trie.root)
                
        return res