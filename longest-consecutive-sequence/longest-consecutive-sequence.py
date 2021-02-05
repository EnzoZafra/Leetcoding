class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
        longestLength = 0
        length = 1
        prev = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num == prev + 1:
                length += 1
            elif num == prev:
                continue
            else:
                longestLength = max(longestLength, length)
                length = 1
            
            prev = num
        
        return max(longestLength, length)
