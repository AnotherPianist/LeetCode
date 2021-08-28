from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter(s2[:len(s1) - 1])
        i = 0
        while i + len(s1) - 1 < len(s2):
            c2[s2[i + len(s1) - 1]] += 1
            if c1 == c2:
                return True
            c2[s2[i]] -= 1
            if c2[s2[i]] == 0:
                del c2[s2[i]]
            i += 1
        return False