class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None
        
        indicies = {x:i for i, x in enumerate(nums)}
        
        for i, num in enumerate(nums):
            diff = target - num
            index = indicies.get(diff, None)
            if index and i != index:
                return [i, index]
        
        return None