class Solution(object):
    # []
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find pivot via BST
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
        
        return nums[start]