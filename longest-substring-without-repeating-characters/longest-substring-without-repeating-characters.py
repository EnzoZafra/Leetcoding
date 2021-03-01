class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        counter = collections.defaultdict(int)
        repeating = 0
        
        longest = 1
        start = 0
        end = 0
        
        while end < len(s):
            endChar = s[end]
            counter[endChar] += 1
            if counter[endChar] > 1:
                repeating += 1
            
            while repeating > 0:
                
                startChar = s[start]
                counter[startChar] -= 1
                if counter[endChar] == 1:
                    repeating -= 1
                
                start += 1
            
            longest = max(longest, end - start + 1)
            end += 1
        
        return longest
                