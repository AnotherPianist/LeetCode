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


class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.contains_key(c):
                node.set(c, TrieNode())
            node = node.get(c)
        node.set_end()

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        
        while stack:
            node, i = stack.pop()
            if i >= len(word) and node.is_end:
                return True
            elif i < len(word) and word[i] == '.':
                for child in node.links:
                    if child:
                        stack.append((child, i + 1))
            elif i < len(word) and node.contains_key(word[i]):
                stack.append((node.get(word[i]), i + 1))
        
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)