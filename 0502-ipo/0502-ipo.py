class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()
        
        priority_queue = []
        available_projects_idx = 0
        
        for _ in range(k):
            while available_projects_idx < len(projects) and projects[available_projects_idx][0] <= w:
                heappush(priority_queue, -projects[available_projects_idx][1])
                available_projects_idx += 1
            if not priority_queue:
                break
            w += -heappop(priority_queue)
        
        return w