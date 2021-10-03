class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, n in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + n)
        return True
            