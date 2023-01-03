class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs) == 1:
            return 0
        
        cols_to_delete = 0

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i - 1][j]:
                    cols_to_delete += 1
                    break

        return cols_to_delete