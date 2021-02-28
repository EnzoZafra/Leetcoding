class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backtrack(start):
            if start == len(nums):
                self.out.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
            
        self.out = []
        backtrack(0)
        return self.out
               