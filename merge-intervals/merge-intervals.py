class Solution(object):
    def getStartAndEndTimes(self, interval):
        return interval[0], interval[1]
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # sort the intervals by their start time
        intervals.sort(key=lambda x:x[0])
        out = [] 
        prev = intervals[0]
        
        for interval in intervals[1:]:
            prevStart, prevEnd = self.getStartAndEndTimes(prev)
            currStart, currEnd = self.getStartAndEndTimes(interval)
            
            if currStart >= prevStart and currStart <= prevEnd:
                prev = [prevStart, max(currEnd, prevEnd)]
            else:
                out.append(prev)
                prev = interval
        out.append(prev)
        return out
            
            
        
        