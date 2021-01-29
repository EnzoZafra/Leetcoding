class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        d[0] = 1
        
        count = 0
        sumSoFar = 0
        
        for num in nums:
            sumSoFar += num
            
            diff = sumSoFar - k
            if diff in d:
                count += d[diff]
                
            d[sumSoFar] = d.get(sumSoFar, 0) + 1
        
        return count