class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return m * n if not ops else min(op[0] for op in ops) * min(op[1] for op in ops)