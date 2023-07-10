class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = curr_sum = 0
        res = float("inf")
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return res if res != float("inf") else 0