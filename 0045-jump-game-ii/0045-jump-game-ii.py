class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur_end = cur_far = 0
        
        for i in range(len(nums) - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                res += 1
                cur_end = cur_far
        
        return res