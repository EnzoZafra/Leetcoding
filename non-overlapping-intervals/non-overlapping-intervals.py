class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[0])
        
        if not intervals:
            return 0
        
        count = 0
        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[0] <= interval[0] and prev[1] > interval[0]:
                count += 1
                
                # keep the one that ends earlier
                if prev[1] > interval[1]:
                    prev = interval 
            else:
                prev = interval
        
        return count