class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def is_subsequence(string, target):
            target = iter(target)
            return all(c in target for c in string)
        
        strs.sort(key=lambda x: -len(x))
        
        for i, word in enumerate(strs):
            if all(not is_subsequence(word, strs[j]) for j in range(len(strs)) if j != i):
                return len(word)
        return -1