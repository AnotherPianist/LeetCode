from collections import Counter, defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        c = Counter(chars)
        m = defaultdict(int)
        for word in words:
            corrects = 0
            for char in word:
                if char not in c:
                    break
                m[char] += 1
                if m[char] > c[char]:
                    break
                corrects += 1
            if corrects == len(word):
                res += len(word)
            m.clear()
        return res