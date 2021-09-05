from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        d = defaultdict(list)
        res = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    d[nums[i] + nums[j] + nums[k]].append(k)
        for i in range(len(nums)):
            for v in d[nums[i]]:
                if i > v:
                    res += 1
        return res