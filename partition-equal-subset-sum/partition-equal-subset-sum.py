class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def recur(start, target_sum):
            if target_sum == 0:
                return True
            
            if target_sum < 0 or start == len(nums):
                return False
            
            if (start, target_sum) in self.memo:
                return self.memo[(start, target_sum)]
            
            chooseItem = recur(start+1, target_sum - nums[start])
            dontChooseItem = recur(start+1, target_sum)
            
            out = chooseItem or dontChooseItem
            self.memo[(start, target_sum)] = out
            
            return out
        
        self.memo = {}
        num_sum = sum(nums)
        
        if num_sum % 2 != 0:
            return False
        
        return recur(0, num_sum/2)
        