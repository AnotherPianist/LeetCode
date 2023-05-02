class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_id, max_time = logs[0]
        
        for i, (id, leave_time) in enumerate(logs):
            if i == 0:
                continue
            
            current_time = leave_time - logs[i - 1][1]
            
            if current_time  >= max_time:
                max_id = min(max_id, id) if current_time == max_time else id
                max_time = current_time
        
        return max_id