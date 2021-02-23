class Solution(object):
    def extremeInsertionIndex(self, nums, target, left):
        start = 0
        end = len(nums)
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                end = mid
            else:
                start = mid + 1
        
        return start
                
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftIndex = self.extremeInsertionIndex(nums, target, True)
        
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        
        rightIndex = self.extremeInsertionIndex(nums, target, False) - 1
        
        return [leftIndex, rightIndex]
        