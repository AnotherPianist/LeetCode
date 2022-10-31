from math import floor


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = sum = 0
        
        for val in nums:
            if val % 6 == 0:
                count += 1
                sum += val
        
        return floor(sum / count) if count != 0 else 0