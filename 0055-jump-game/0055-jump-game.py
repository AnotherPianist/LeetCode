class Solution:
    def canJump(self, nums: List[int]) -> bool:
        min_jump = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= min_jump:
                min_jump = i
        
        return min_jump <= 0