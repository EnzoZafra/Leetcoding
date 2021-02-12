class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        maxLen = 0
        start = 0
        end = 0
        
        while end < len(s):
            endChar = s[end]
            counter[endChar] = counter.get(endChar, 0) + 1
            
            while counter[endChar] > 1:
                startChar = s[start]
                counter[startChar] = counter.get(startChar, 0) - 1
                start += 1
            
            maxLen = max(maxLen, end-start+1)
            end += 1
        
        return maxLen