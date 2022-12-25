from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        res = []
        
        for query in queries:
            index = bisect_right(nums, query)
            res.append(index)
        
        return res