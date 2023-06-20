class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        subarray_len = 2 * k + 1
        averages = [-1] * n
        
        if subarray_len > n:
            return averages
        
        prefix_sum = [0]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        for i in range(k, n - k):
            left, right = i - k, i + k
            averages[i] = (prefix_sum[right + 1] - prefix_sum[left]) // subarray_len
        
        return averages