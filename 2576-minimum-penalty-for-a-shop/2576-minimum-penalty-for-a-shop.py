class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = curr_penalty = 0
        earliest_hour = 0

        for i, val in enumerate(customers):
            if val == 'Y':
                curr_penalty -= 1
            else:
                curr_penalty += 1
            
            if curr_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = curr_penalty
        
        return earliest_hour