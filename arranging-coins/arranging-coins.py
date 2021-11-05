from math import sqrt, floor


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # left, right = 0, n
        # while left <= right:
        #     mid = left + ((right - left) // 2)
        #     result = mid * (mid + 1) // 2
        #     if result == n:
        #         return mid
        #     elif result > n:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return right
        
        return floor(sqrt(2 * n + 0.25) - 0.5)
        