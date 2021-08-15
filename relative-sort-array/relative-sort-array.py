class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = {val: i for i, val in enumerate(arr2)}
        return sorted(arr1, key=lambda val: m.get(val, len(arr2) + val))