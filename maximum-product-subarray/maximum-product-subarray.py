class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        minSoFar = nums[0]
        maxSoFar = nums[0]
        result = maxSoFar
        
        for curr in nums[1:]:
            temp = max(curr, max(maxSoFar*curr, minSoFar*curr))
            minSoFar = min(curr, min(maxSoFar*curr, minSoFar*curr))
            
            maxSoFar = temp
            result = max(maxSoFar, result)
        
        return result