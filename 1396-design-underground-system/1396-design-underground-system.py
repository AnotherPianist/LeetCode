from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(list)
        self.start_times = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_times[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.start_times[id]
        self.times[(start_station, stationName)].append(t - start_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.times[(startStation, endStation)]
        
        return sum(times) / len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)