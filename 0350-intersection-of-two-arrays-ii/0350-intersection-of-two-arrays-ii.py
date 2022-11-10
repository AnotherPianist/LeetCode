from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1) if len(nums1) >= len(nums2) else Counter(nums2)
        res = []
        
        for num in nums2 if len(nums2) <= len(nums1) else nums1:
            if c[num] > 0:
                res.append(num)
                c[num] -= 1
                
        return res