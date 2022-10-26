class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {0: 0}
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if sum % k not in m:
                m[sum % k] = i + 1
            elif m[sum % k] < i:
                return True
        return False