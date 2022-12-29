from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enqueue, processing, i) for i, (enqueue, processing) in enumerate(tasks)]
        tasks.sort()

        next_tasks = []
        curr_time = tasks[0][0]
        i = 0

        order_idxs = []

        while i < len(tasks) or next_tasks:
            if not next_tasks and curr_time < tasks[i][0]:
                curr_time = tasks[i][0]
            while i < len(tasks) and curr_time >= tasks[i][0]:
                heappush(next_tasks, (tasks[i][1], tasks[i][2]))
                i += 1
            end_time, idx = heappop(next_tasks)
            curr_time += end_time
            order_idxs.append(idx)

        return order_idxs