from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join(ch * n for ch, n in c.most_common())