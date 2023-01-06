class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        
        for i, price in enumerate(costs):
            if total + price > coins:
                return i
            total += price
        return i + 1