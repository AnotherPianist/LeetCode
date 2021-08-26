class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        i, j = 0, len(nums) - 1
        k = len(nums) - 1
        while i <= j:
            if nums[i] ** 2 > nums[j] ** 2:
                res[k] = nums[i] ** 2
                i += 1
            else:
                res[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return res