class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
        
        i = 1
        
        for j in range(1, len(nums)):
            if nums[j - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
                
        return i