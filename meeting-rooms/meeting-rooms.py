class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x[0])
        
        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[0] <= interval[0] < prev[1]:
                return False
            prev = interval
        
        return True