from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        
        for s, (r, c) in enumerate(stones):
            rows[r].append(s)
            cols[c].append(s)

        seen = set()

        def dfs(s):
            if s in seen:
                return 0
            seen.add(s)
            r, c = stones[s]
            for ss in chain(rows[r], cols[c]):
                dfs(ss)
            return 1
                
        c = sum(dfs(s) for s in range(len(stones)))

        return len(stones) - c