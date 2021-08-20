class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = [None] * len(s)
        for i, c in enumerate(s):
            new_string[indices[i]] = c
        return "".join(new_string)