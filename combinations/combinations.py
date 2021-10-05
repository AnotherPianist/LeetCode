class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(nums, k, path):
            if len(path) == k:
                res.append(path)
                return 
            for i in range(len(nums)):
                dfs(nums[i+1:], k, path+[nums[i]])
        
        dfs(list(range(1, n+1)), k, [])
        return res