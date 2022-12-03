from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return "".join(sorted(list(s), key=lambda c: (-counter[c], c)))