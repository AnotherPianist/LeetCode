class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        sorted_data = sorted((num, c) for num, c in zip(nums, cost))
        n = len(cost)
        
        prefix_cost = [sorted_data[0][1]]
        for i in range(1, n):
            prefix_cost.append(prefix_cost[-1] + sorted_data[i][1])
        
        total_cost = 0
        
        for i in range(1, n):
            total_cost += sorted_data[i][1] * (sorted_data[i][0] - sorted_data[0][0])
        res = total_cost
        
        for i in range(1, n):
            gap = sorted_data[i][0] - sorted_data[i - 1][0]
            total_cost += prefix_cost[i - 1] * gap
            total_cost -= gap * (prefix_cost[n - 1] - prefix_cost[i - 1])
            res = min(res, total_cost)
        
        return res