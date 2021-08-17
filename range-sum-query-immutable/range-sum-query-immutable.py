class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [nums[0]]
        if len(nums) > 1:
            for num in nums:
                self.sums.append(self.sums[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        if len(self.sums) == 1:
            return self.sums[0]
        return self.sums[right + 1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)