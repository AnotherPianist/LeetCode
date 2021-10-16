class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy = float('inf')
        one_profit = two_profit = 0
        for price in prices:
            one_buy = min(one_buy, price)
            one_profit = max(one_profit, price - one_buy)
            two_buy = min(two_buy, price - one_profit)
            two_profit = max(two_profit, price - two_buy)
        return two_profit
            