class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [] 
        def helper(arr, start):
            out.append(arr[:])
            
            for i in range(start, len(nums)):
                arr.append(nums[i])
                helper(arr, i+1)
                arr.pop()
        
        helper([], 0)
        return out
                