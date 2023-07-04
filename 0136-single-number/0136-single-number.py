class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cummulative_xor = 0
        
        for num in nums:
            cummulative_xor ^= num
        
        return cummulative_xor