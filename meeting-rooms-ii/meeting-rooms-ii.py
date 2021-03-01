class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = [x[0] for x in intervals]
        ends = [x[1] for x in intervals]
        
        starts.sort()
        ends.sort()
        
        currEnd = 0
        rooms = 0
        for start in starts:
            if start < ends[currEnd]:
                rooms += 1 
            else:
                currEnd += 1
        
        return rooms
