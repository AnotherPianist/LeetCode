class Solution:
    def average(self, salary: List[int]) -> float:
        min_val, max_val = float("inf"), float("-inf")
        sum = 0
        for i, val in enumerate(salary):
            min_val = min(min_val, val)
            max_val = max(max_val, val)
            sum += val
        return (sum - min_val - max_val) / (i - 1)