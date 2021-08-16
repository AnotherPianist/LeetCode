from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        m = Counter(s1.split())
        m += Counter(s2.split())
        return [word for word in m if m[word] == 1]