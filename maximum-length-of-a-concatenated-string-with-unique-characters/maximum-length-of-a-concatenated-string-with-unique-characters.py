class Solution(object):
    def isUnique(self, string):
        seen = set()
        for char in string:
            if char in seen:
                return False
            else:
                seen.add(char)
                
        return True
        
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        dp = [set()]
        maxLen = 0
        
        for sub in arr:
            if not self.isUnique(sub):
                continue
            
            currUsed = set(sub)
            for previousSets in dp[:]:
                # if there is an intersection with the set, skip
                if currUsed & previousSets:
                    continue 
                    
                # append the union
                union = currUsed | previousSets
                dp.append(union)
                
                maxLen = max(maxLen, len(union))
                
                #print(dp)
        return maxLen
          
        
