class UndergroundSystem:

    def __init__(self):
        self.inTransit = {}
        self.history = collections.defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.inTransit:
            return None
        
        else:
            self.inTransit[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_station, in_time = self.inTransit[id]
        del self.inTransit[id]
        
        key = (in_station, stationName)
        total_time = t - in_time
        
        self.history[key].append(total_time)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        times = self.history[key]
        
        return sum(times)/len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)