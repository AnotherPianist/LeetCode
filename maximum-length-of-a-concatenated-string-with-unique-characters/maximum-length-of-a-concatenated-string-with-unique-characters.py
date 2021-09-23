class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def dfs(i, formed):
            if len(formed) != len(set(formed)):
                return 0
            best = len(formed)
            for j in range(i, len(arr)):
                best = max(best, dfs(j + 1, formed + arr[j]))
            return best
        
        return dfs(0, "")