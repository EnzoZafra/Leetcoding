class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # sort by identifier
        letters.sort(key = lambda x: x.split()[0])
        # sort by suffix
        letters.sort(key = lambda x: x.split()[1:])
        
        result = letters + digits
        return result