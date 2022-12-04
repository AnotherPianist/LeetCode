from collections import Counter


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        dp = [Counter() for item in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += (dp[j][nums[i] - nums[j]] + 1)      
            total += sum(dp[i].values())
          
        return total - (len(nums) - 1) * len(nums) // 2  