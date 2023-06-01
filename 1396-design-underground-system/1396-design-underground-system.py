from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(lambda: (0, 0))
        self.start_times = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_times[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.start_times[id]
        del self.start_times[id]

        prev_time, prev_count = self.times[(start_station, stationName)]
        self.times[(start_station, stationName)] = (prev_time + t - start_time, prev_count + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.times[(startStation, endStation)]
        
        return time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)