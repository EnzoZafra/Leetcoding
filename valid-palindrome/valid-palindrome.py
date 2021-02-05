class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # trim whitespace at beginning and end
        s.strip()
        
        # trim whitespace in between
        s = s.replace(' ', '')
        
        if not s:
            return True
        
        start = 0
        end = len(s) - 1
        while start < end:
            charStart = s[start]
            charEnd = s[end]
            if charStart.isalnum() and charEnd.isalnum():
                if charStart.lower() != charEnd.lower():
                    return False
                start += 1
                end -= 1
            elif not charStart.isalnum():
                start += 1 
            elif not charEnd.isalnum():
                end -= 1 
        
        return True