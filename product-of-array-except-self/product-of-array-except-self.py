class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [1 for _ in range(len(nums))]
        
        # left products
        for i in range(1, len(nums)):
            num = nums[i-1]
            out[i] = out[i-1] * num
        
        R = 1
        # multiply the right products
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * R
            R = R * nums[i]
        
        return out