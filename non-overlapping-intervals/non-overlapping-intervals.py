class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        out = 0
        intervals.sort(key=lambda x:x[0])
        
        prev = intervals[0]
        for interval in intervals[1:]:
            start = prev[0]
            end = prev[1]
            
            # if the previous interval isnt done yet and the new one is starting
            if end > interval[0]:
                out += 1
                
                # keep the new one
                if end > interval[1]:
                    prev = interval
            else:
                prev = interval 
        
        return out