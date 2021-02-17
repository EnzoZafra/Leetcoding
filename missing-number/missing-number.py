class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        numsSet = set(nums)
        for i in range(len(nums)+1):
            if i not in numsSet:
                return i
        
        return -1