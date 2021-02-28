class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        occ = Counter(t)
        count = len(occ)
        
        start = 0
        end = 0
        
        out = ''
        minWindowSize = float('inf')
        
        while end < len(s):
            endChar = s[end]
            
            if endChar in occ:
                occ[endChar] -= 1
                if occ[endChar] == 0:
                    count -= 1
            
            # start shrinking window
            while count == 0:
                if end - start + 1 < minWindowSize:
                    minWindowSize = end - start + 1
                    out = s[start:end+1]
                
                startChar = s[start]
                if startChar in occ:
                    if occ[startChar] == 0:
                        count += 1
                        
                    occ[startChar] += 1
                    
                start += 1
            end += 1
        
        return out
