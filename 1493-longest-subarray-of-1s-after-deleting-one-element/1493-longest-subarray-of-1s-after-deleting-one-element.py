class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = longest_window = 0
        last_zero = -1
        
        for i, num in enumerate(nums):
            if num == 0:
                start = last_zero + 1
                last_zero = i
            longest_window = max(longest_window, i - start)

        return longest_window
