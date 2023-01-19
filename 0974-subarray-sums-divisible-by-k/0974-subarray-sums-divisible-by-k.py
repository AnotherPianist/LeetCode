class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod = result = 0
        
        mod_groups = [0] * k
        mod_groups[0] = 1
        
        for num in nums:
            prefix_mod = (prefix_mod + num) % k
            result += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1
        
        return result