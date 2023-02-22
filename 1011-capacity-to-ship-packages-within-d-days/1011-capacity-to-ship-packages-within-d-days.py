class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            days_needed, load = 1, 0
            
            for weight in weights:
                load += weight
                if load > capacity:
                    days_needed += 1
                    load = weight
            
            return days_needed <= days
        
        
        max_weight, total_weight = 0, 0
        
        for weight in weights:
            max_weight = max(max_weight, weight)
            total_weight += weight
        
        l, r = max_weight, total_weight
        
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l