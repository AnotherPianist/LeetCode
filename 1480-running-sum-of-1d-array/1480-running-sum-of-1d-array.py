class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            if len(res) == 0:
                res.append(num)
            else:
                res.append(res[-1] + num)
        
        return res