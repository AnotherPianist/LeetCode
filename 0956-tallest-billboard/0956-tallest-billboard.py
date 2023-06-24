from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        
        for r in rods:
            new_dp = dp.copy()
            
            for diff, taller in dp.items():
                shorter = taller - diff
                new_dp[diff + r] = max(new_dp[diff + r], taller + r)
                
                new_diff = abs(shorter + r - taller)
                new_taller = max(taller, shorter + r)
                new_dp[new_diff] = max(new_dp[new_diff], new_taller)
            
            dp = new_dp
        
        return dp[0]