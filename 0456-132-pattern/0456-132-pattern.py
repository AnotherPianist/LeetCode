class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        n = len(nums)
        min_array = [-1] * n
        min_array[0] = nums[0]

        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])
        
        k = n
        for j in range(n - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while k < n and nums[k] <= min_array[j]:
                k += 1
            if k < n and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        
        return False
