from math import gcd


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        max_states = 2 ** len(nums)
        mask = max_states - 1
        
        dp = [0] * max_states
        
        for state in range(mask, -1, -1):
            if state == mask:
                dp[state] = 0
                continue
            
            numbers_taken = bin(state).count('1')
            pairs_formed = numbers_taken // 2
            
            if numbers_taken % 2 != 0:
                continue
            
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (state >> i & 1) == 1 or (state >> j & 1) == 1:
                        continue
                    current_score = (pairs_formed + 1) * gcd(nums[i], nums[j])
                    state_after = state | (1 << i) | (1 << j)
                    remaining_score = dp[state_after]
                    dp[state] = max(dp[state], current_score + remaining_score)
        
        return dp[0]