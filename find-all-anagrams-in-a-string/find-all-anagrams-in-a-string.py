class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        out = []
        start = 0
        end = 0
        
        counter = Counter(p)
        count = len(counter)
        
        while end < len(s):
            endChar = s[end]
            counter[endChar] -= 1
            if counter[endChar] == 0:
                count -= 1
            
            end += 1
            while count == 0:
                if end - start == len(p):
                    out.append(start)
                
                startChar = s[start]
                 
                if counter[startChar] == 0:
                    count += 1
                counter[startChar] += 1
                
                start += 1
        
        return out
            