class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        
        seen = set()
        deletions = 0
        
        for k in counter.values():
            while k in seen:
                k -= 1
                deletions += 1
            if k > 0:
                seen.add(k)
        return deletions