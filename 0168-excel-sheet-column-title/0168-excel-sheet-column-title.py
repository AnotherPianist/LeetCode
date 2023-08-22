from collections import deque


class Solution:
    def convertToTitle(self, column_number: int) -> str:
        chars = deque()

        while column_number != 0:
            column_number -= 1
            chars.appendleft(chr(ord('A') + column_number % 26))
            column_number //= 26
        
        return "".join(chars)