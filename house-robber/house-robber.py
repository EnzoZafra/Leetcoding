class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        robbedSoFar = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            num = nums[i]
            
            robThisPlace = num + robbedSoFar[i-2] if i-2 >= 0 else num
            doNotRob = robbedSoFar[i-1] if i-1>=0 else 0
            
            robbedSoFar[i] = max(robThisPlace, doNotRob)
        
        return max(robbedSoFar)
        
        