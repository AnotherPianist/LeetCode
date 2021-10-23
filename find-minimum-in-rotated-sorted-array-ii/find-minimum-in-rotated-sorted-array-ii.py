class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i, j = 0, len(nums) - 1
        if nums[j] > nums[0]:
            return nums[0]
        
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                j -= 1
        return nums[j]