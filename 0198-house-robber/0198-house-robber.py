class Solution:
    def rob(self, nums: List[int]) -> int:
        last = now = 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now