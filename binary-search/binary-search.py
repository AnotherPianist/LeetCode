class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1