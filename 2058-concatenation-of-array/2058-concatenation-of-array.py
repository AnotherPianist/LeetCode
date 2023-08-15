class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(2 * n):
            ans.append(nums[i % n])
        
        return ans