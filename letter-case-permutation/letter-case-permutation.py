class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l = []

        def backtrack(st, i):
            if i == len(s):
                l.append(''.join(st))
                return
            if st[i].isnumeric():
                backtrack(st, i + 1)
            else:
                st[i] = st[i].lower()
                backtrack(st, i + 1)
                st[i] = st[i].upper()
                backtrack(st, i + 1)

        backtrack(list(s), 0)
        return l
