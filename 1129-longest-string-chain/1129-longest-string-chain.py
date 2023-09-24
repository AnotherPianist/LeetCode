from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda word: len(word))
        graph = defaultdict(set)

        for i, word in enumerate(words):
            for j in range(len(word)):
                graph[word[:j] + word[j + 1:]].add(i)
        
        dists = [1] * n
        res = 1

        for u in range(n):
            for v in graph[words[u]]:
                dists[v] = max(dists[v], dists[u] + 1)
                res = max(res, dists[v])
        
        return res
