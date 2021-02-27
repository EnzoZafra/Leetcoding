class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumTotal = 0
        for i in range(len(nums)+1):
            sumTotal += i
        
        for num in nums:
            sumTotal -= num
        
        return sumTotal