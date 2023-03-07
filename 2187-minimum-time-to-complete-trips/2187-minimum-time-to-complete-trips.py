class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def is_enough_time(given_time):
            trips = 0
            
            for t in time:
                trips += given_time // t

            return trips >= totalTrips


        left, right = 1, max(time) * totalTrips
        
        while left < right:
            mid = left + (right - left) // 2
            
            if is_enough_time(mid):
                right = mid
            else:
                left = mid + 1
        
        return left