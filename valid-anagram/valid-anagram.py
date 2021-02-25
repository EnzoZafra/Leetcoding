class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counterS = Counter(s)
        counterT = Counter(t)
        
        for char in counterS:
            countS = counterS.get(char, 0)
            countT = counterT.get(char, 0)
            
            if countS != countT:
                return False
            
        for char in counterT:
            countS = counterS.get(char, 0)
            countT = counterT.get(char, 0)
            
            if countS != countT:
                return False
                
        
        return True