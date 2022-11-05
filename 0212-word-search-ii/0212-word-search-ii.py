from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.count = 0
        self.is_end = False
        
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node.links[c].count += 1
            node = node.links[c]
        node.is_end = True
        
    def remove(self, word):
        node = self.root
        for c in word:
            if c in node.links:
                node.links[c].count -= 1
                if node.links[c].count == 0:
                    del node.links[c]
                node = node.links[c]
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        
        def dfs(i, j, formed, node):
            if node.is_end:
                res.append(formed)
                node.is_end = False
                trie.remove(formed)
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