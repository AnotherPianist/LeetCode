class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set(arr)
        
        for i in range(1, k + len(arr) + 1):
            if i not in nums:
                k -= 1
            if k == 0:
                return i