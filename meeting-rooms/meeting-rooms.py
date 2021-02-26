class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        # sort by start times
        intervals.sort(key=lambda x: x[0])
        
        prev = intervals[0]
        
        for interval in intervals[1:]:
            start = prev[0]
            end = prev[1]
            
            if start <= interval[0] < end:
                return False
            
            prev = interval
        
        return True
            
        
        