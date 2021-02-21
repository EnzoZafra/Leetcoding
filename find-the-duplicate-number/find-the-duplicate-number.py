class Solution(object):
    def findDuplicateTemp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        actualSum = sum(nums)
        expectedSum = 0
        
        for i in range(1, maxNum+1):
            expectedSum += i
        
        return actualSum - expectedSum
    
    def findDuplicate(self, nums):
        seen = set() 
        
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        
        return -1