class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_idx = odd_idx = 0

        while even_idx < n and odd_idx < n:
            if nums[odd_idx] % 2 == 0:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                even_idx += 1
            odd_idx += 1
        
        return nums