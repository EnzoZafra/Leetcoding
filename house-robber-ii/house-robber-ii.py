class Solution(object):
    def rob_twoptr(self, nums):
        t1 = 0
        t2 = 0
        
        for num in nums:
            temp = t1
            t1 = max(num + t2, t1)
            t2 = temp
        return t1
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob_twoptr(nums[:-1]), self.rob_twoptr(nums[1:]))
        
        