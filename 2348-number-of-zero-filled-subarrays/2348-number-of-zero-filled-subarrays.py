class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = current_sequence = 0
        
        for num in nums:
            current_sequence = 0 if num != 0 else current_sequence + 1
            res += current_sequence
        
        return res