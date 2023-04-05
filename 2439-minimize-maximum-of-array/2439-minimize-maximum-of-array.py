from math import ceil


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            res = max(res, ceil(prefix_sum / (i + 1)))
        
        return res