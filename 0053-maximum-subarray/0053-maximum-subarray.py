class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = max_until_now = -inf
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_until_now = max(curr_max, max_until_now)
        return max_until_now