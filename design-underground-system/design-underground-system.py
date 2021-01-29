class CheckInItem(object):
    def __init__(self, station, time):
        self.station = station
        self.time = time

class UndergroundSystem(object):

    def __init__(self):
        self.checkedIn = {}
        self.avgTimes = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkedIn[id] = CheckInItem(stationName, t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        sourceNode = self.checkedIn[id]
        del self.checkedIn[id]
        duration = t - sourceNode.time
        
        timeKey = sourceNode.station + "->" + stationName
        
        avgTimesList = self.avgTimes.get(timeKey, [])
        avgTimesList.append(duration)
        self.avgTimes[timeKey] = avgTimesList

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        # should hash the key?
        timeKey = startStation + "->" + endStation
        avgTimesList = self.avgTimes[timeKey]
        print(avgTimesList)
        return float(sum(avgTimesList)) / float(len(avgTimesList))
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)