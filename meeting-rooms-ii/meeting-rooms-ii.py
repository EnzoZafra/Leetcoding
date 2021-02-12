class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        
        starts.sort()
        ends.sort()
        
        rooms = 0
        
        endPtr = 0
        startPtr = 0
        
        while startPtr < len(intervals):
            if starts[startPtr] >= ends[endPtr]:
                rooms -= 1
                endPtr += 1
                
            rooms += 1
            startPtr += 1
       
        return rooms
             
        