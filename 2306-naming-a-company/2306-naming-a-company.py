class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffixes = [set() for _ in range(26)]
        res = 0
        
        for idea in ideas:
            suffixes[ord(idea[0]) - ord('a')].add(idea[1:])
        
        for i in range(25):
            for j in range(i + 1, 26):
                if len(suffixes[i]) > 0 and len(suffixes[j]) > 0:
                    union_length = len(suffixes[i] & suffixes[j])
                    res += 2 * (union_length - len(suffixes[i])) * (union_length - len(suffixes[j]))
        
        return res