class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = current_sum = 0
        for num in nums:
            current_sum += num
            min_val = min(min_val, current_sum)
        return -min_val + 1