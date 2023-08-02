class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 1
        
        for num in arr:
            previous_length = dp.get(num - difference, 0)
            dp[num] = previous_length + 1
            max_length = max(max_length, dp[num])
        
        return max_length
                