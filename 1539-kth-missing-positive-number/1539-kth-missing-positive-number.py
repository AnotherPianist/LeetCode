# class Solution:
# def findKthPositive(self, arr: List[int], k: int) -> int:
#         nums = set(arr)
        
#         for i in range(1, k + len(arr) + 1):
#             if i not in nums:
#                 k -= 1
#             if k == 0:
#                 return i


# ------------------------------------------------------------
#                       Binary Search
# ------------------------------------------------------------
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
            
        return left + k