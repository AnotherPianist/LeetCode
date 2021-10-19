class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, stack = {}, []
        for num in nums2:
            while stack and stack[-1] < num:
                m[stack.pop()] = num
            stack.append(num)
        return [m.get(num, -1) for num in nums1]