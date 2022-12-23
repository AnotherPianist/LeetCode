class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        have = cool = float('-inf')
        for price in prices:
            free, have, cool = max(free, cool), max(have, free - price), have + price
        return max(free, cool)
