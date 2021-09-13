from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        c['l'] = math.floor(c['l'] / 2)
        c['o'] = math.floor(c['o'] / 2)
        return min(c[char] for char in "balloon")