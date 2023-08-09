class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        
        def count_valid_pairs(threshold):
            i = count = 0
            
            while i < n - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    count += 1
                    i += 1
                i += 1
            
            return count
        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            
            if count_valid_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        
        return left