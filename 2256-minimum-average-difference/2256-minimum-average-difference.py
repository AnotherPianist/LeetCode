class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:        
        total = sum(nums)
        min_avg_diff = float("inf")
        curr_sum = 0
        idx = -1
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            left_avg = curr_sum // (i + 1)
            right_avg = 0
            if i != len(nums) - 1:
                right_avg = (total - curr_sum) // (len(nums) - i - 1)
            avg_diff = abs(left_avg - right_avg)
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                idx = i
                
        return idx
            