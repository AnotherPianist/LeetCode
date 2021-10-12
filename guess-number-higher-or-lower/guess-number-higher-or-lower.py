# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right, middle = 1, n, n // 2
        clue = -1
        while clue != 0:
            clue = guess(middle)
            if clue == 0:
                return middle
            elif clue < 0:
                right = middle - 1
            else:
                left = middle + 1
            middle = left + (right - left) // 2
        