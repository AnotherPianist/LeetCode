class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False
        
    def contains_key(self, key):
        return bool(self.links[ord(key) - ord('a')])
    
    def get(self, key):
        return self.links[ord(key) - ord('a')]
    
    def set(self, key, node):
        self.links[ord(key) - ord('a')] = node
    
    def set_end(self):
        self.is_end = True


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.contains_key(c):
                node.set(c, TrieNode())
            node = node.get(c)
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.contains_key(c):
                return False
            node = node.get(c)
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.contains_key(c):
                return False
            node = node.get(c)
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)