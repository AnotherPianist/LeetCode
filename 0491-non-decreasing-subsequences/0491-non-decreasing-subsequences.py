class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seq = []
        
        def backtrack(i):
            if i == len(nums):
                if len(seq) >= 2:
                    res.add(tuple(seq))
                return
            if not seq or seq[-1] <= nums[i]:
                seq.append(nums[i])
                backtrack(i + 1)
                seq.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res