class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sum_left = 0
        
        for i, num in enumerate(nums):
            if sum_left == total - sum_left - num:
                return i
            sum_left += num
        
        return -1