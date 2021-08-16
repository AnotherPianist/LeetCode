from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = Counter(nums)
        for i in range(m.get(0, 0)):
            nums[i] = 0
        for i in range(m.get(0, 0), m.get(0, 0) + m.get(1, 0)):
            nums[i] = 1
        for i in range(m.get(0, 0) + m.get(1, 0), m.get(0, 0) + m.get(1, 0) + m.get(2, 0)):
            nums[i] = 2