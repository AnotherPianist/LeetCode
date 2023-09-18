class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        strengths.sort()
        return [i for strength, i in strengths[:k]]