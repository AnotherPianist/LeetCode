class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        subarray_len = 2 * k + 1
        averages = [-1] * n
        
        if subarray_len > n:
            return averages
        
        window_sum = sum(nums[i] for i in range(subarray_len))
        averages[k] = window_sum // subarray_len

        for i in range(subarray_len, n):
            window_sum = window_sum - nums[i - subarray_len] + nums[i]
            averages[i - k] = window_sum // subarray_len
        
        return averages