class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(base):
            return sum(abs(base - num) * c for num, c in zip(nums, cost))
        
        left = right = nums[0]
        for num in nums:
            left = min(left, num)
            right = max(right, num)
            
        res = get_cost(left)
        
        while left < right:
            mid = left + (right - left) // 2
            cost_1, cost_2 = get_cost(mid), get_cost(mid + 1)
            
            res = min(cost_1, cost_2)
            
            if cost_1 > cost_2:
                left = mid + 1
            else:
                right = mid
        
        return res