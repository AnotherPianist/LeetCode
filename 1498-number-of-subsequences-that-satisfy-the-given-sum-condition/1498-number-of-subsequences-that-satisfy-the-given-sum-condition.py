from bisect import bisect_right


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = 0
        
        for left in range(len(nums)):
            right = bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                res += 2 ** (right - left)
        
        return res % 1000000007