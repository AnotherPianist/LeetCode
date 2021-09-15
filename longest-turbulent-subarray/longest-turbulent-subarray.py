class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        def cmp(a, b):
            return (a > b) - (a < b)
        
        res = 1
        i = 0
        for j in range(1, len(arr)):
            if cmp(arr[j - 1], arr[j]) == 0:
                i = j
            elif j == len(arr) - 1 or cmp(arr[j - 1], arr[j]) * cmp(arr[j], arr[j + 1]) != -1:
                res = max(res, j - i + 1)
                i = j
        return res