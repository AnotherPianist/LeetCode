class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        def dfs(nums):
            n = len(nums)
            
            if n < 3:
                return 1
            
            left_nodes = [num for num in nums if num < nums[0]]
            right_nodes = [num for num in nums if num > nums[0]]
            
            return dfs(left_nodes) * dfs(right_nodes) * comb(n - 1, len(left_nodes)) % mod
    
        return int((dfs(nums) - 1) % mod)