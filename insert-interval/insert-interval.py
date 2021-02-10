class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        out = []
        start = newInterval[0]
        end = newInterval[1]
        
        # get all the ones that start before newInterval
        
        i = 0 
        while i < len(intervals) and intervals[i][0] < start:
            out.append(intervals[i])
            i += 1
        
        # insert our new interval
        # if the end of the last interval is earlier than the start of new interval, just add 
        if not out or out[-1][1] < start:
            out.append(newInterval) 
        else:
            out[-1][1] = max(out[-1][1], end)
        
        while i < len(intervals):
            interval = intervals[i]
            i += 1
            
            if out[-1][1] < interval[0]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
        
        return out
            