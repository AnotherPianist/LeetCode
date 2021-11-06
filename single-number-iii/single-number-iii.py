class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        all_xor = reduce(xor, nums)
        non_zero = all_xor & (all_xor - 1) ^ all_xor
        res1 = reduce(xor, filter(lambda x: x & non_zero, nums))
        return [res1, all_xor ^ res1]