class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        m = {}
        res = []
        for i, num in enumerate(nums):
            m[num] = i
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if -(num1 + nums[j]) in m and m[-(num1 + nums[j])] > j:
                    triplet = [num1, nums[j], -(num1 + nums[j])]
                    if triplet not in res:
                        res.append(triplet)
        return res