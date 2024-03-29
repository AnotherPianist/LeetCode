class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            a = (left + right) // 2
            b = (m + n + 1) // 2 - a

            max_left_a = float('-inf') if a == 0 else nums1[a - 1]
            min_right_a = float('inf') if a == m else nums1[a]
            max_left_b = float('-inf') if b == 0 else nums2[b - 1]
            min_right_b = float('inf') if b == n else nums2[b]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 0:
                    return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2
                else:
                    return max(max_left_a, max_left_b)
            elif max_left_a > min_right_b:
                right = a - 1
            else:
                left = a + 1
