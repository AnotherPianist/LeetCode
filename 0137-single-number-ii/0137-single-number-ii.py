class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        msb = lsb = 0
        
        for num in nums:
            lsb, msb = (~msb & ~lsb & num) | (lsb & ~num), (lsb & num) | (msb & ~num)
        
        return lsb