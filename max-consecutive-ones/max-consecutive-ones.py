class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
        return max_count