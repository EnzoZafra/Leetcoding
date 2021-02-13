class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # sliding window
        # grow window by moving end pointer to the right until we meet the constraint
        # keep growing until we break the constraint
        
        # compress the window by moving the start pointer to the right until we meet the constraint again
        
        if not s or not t:
            return ''
        
        occ = Counter(t)
        counter = len(occ) 

        start = 0
        end = 0
        minWindow = '' 
        minWindowLength = float('inf')
        
        while end < len(s):
            endChar = s[end] 
            
            if endChar in occ:
                occ[endChar] -= 1
                if occ[endChar] == 0:
                    counter -= 1
                    
            while counter == 0:
                if (end - start + 1 < minWindowLength):
                    minWindowLength = end - start + 1
                    minWindow = s[start:end+1]
                    
                startChar = s[start]
                if startChar in occ:
                    if occ[startChar] == 0:
                        counter += 1
                    occ[startChar] += 1
                    
                start += 1
            end += 1

        return minWindow
                
            