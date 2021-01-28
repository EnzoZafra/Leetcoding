class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
       
        out = []
        
        # O(nlogn)
        intervals.sort(key=lambda x: x[0])
        
        currentInterval = intervals[0]
        for interval in intervals[1:]: 
            if interval[0] > currentInterval[1]:
                out.append(currentInterval)
                currentInterval = interval
            else:
                currentInterval[1] = max(currentInterval[1], interval[1])
        
        out.append(currentInterval)
        return out
        
        
        