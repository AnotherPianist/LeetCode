from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def get_notification_time(i):
            if (manager_id := manager[i]) != -1:
                return informTime[manager_id] + get_notification_time(manager_id)
            else:
                return 0

        return max(get_notification_time(i) for i in range(n))