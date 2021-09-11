class Solution:
    def calculate(self, s: str) -> int:
        res = i = 0
        signs = [1, 1]
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += signs.pop() * int(s[start:i])
                continue
            elif s[i] == '-' or s[i] == '+' or s[i] == '(':
                signs.append(signs[-1] * (1, -1)[s[i] == '-'])
            elif s[i] == ')':
                signs.pop()
            i += 1
        return res