class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # length of substring - number of times of the maximum occuring character in the string <= k
        counts = collections.defaultdict(int)
        start = 0
        end = 0
        maxCharCount = 0
        n = len(s)
        out = 0
        
        for end in range(n):
            endChar = s[end]
            counts[endChar] += 1
            maxCharCount = max(maxCharCount, counts[endChar])
            
            substringlen = end - start + 1 
            if substringlen - maxCharCount > k:
                startChar = s[start]
                counts[startChar] -= 1
                start += 1
            
            out = max(out, end-start+1) 
        
        return out
           
                
            