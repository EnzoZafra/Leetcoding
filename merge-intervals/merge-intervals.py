class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x:x[0])
        
        if not intervals:
            return []
        
        out = [] 
        for interval in intervals:
            
            if not out:
                out.append(interval)
                
            else:
                prev_start = out[-1][0]
                prev_end = out[-1][1]
                
                new_start = interval[0]
                new_end = interval[1]
                
                if prev_start <= new_start <= prev_end:
                    out[-1][0] = min(prev_start, new_start)
                    out[-1][1] = max(prev_end, new_end)
                else:
                    out.append(interval)
                    
        return out
        
