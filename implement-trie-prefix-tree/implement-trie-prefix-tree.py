class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False
    
    def containsKey(self, c):
        return bool(self.links[ord(c) - ord('a')])
    
    def get(self, c):
        return self.links[ord(c) - ord('a')]
    
    def put(self, c, node):
        self.links[ord(c) - ord('a')] = node
        
    def setEnd(self):
        self.isEnd = True
        
    # def isEnd(self):
    #     return self.isEnd


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.containsKey(c):
                node.put(c, TrieNode())
            node = node.get(c)
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.containsKey(c):
                return False
            node = node.get(c)
        return node and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.containsKey(c):
                return False
            node = node.get(c)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)