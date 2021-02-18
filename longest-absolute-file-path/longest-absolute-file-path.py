class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        inputArray = input.split('\n')
        
        maxLen = 0
        pathlen = {0:0}
        
        for item in inputArray:
            tabCount = item.count('\t')
            name = item.lstrip('\t')
            
            if '.' in name:
                length = pathlen[tabCount] + len(name)
                maxLen = max(maxLen, length)
            else:
                # add 1 for the '/'
                pathlen[tabCount + 1] = pathlen[tabCount] + len(name) + 1

            print(item, pathlen)
        
        return maxLen
                
        