class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_count = 0
        s = set()
        for idx in range(len(nums)):
            count = 0
            while nums[idx] not in s:
                s.add(nums[idx])
                count += 1
                idx = nums[idx]
            max_count = max(count, max_count)
        return max_count