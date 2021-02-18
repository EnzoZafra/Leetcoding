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
        
        def recur(concatenated, start):
            if self.isUnique(concatenated):
                self.maxLen = max(self.maxLen, len(concatenated))     
            
            for i in range(start, len(arr)):
                concat = concatenated + arr[i]
                recur(concat, i+1)
                concat = concatenated
                
        self.maxLen = 0 
        recur('', 0)
        return self.maxLen