class Solution(object):
    def find_pivot(self, nums):
        # to find the index where the sorted array is rotated
        
        start = 0
        end = len(nums) - 1

        if nums[start] < nums[end]:
            return 0
        
        while start <= end:
            mid = (end + start) // 2
            
            # pivot is somewhere on the right side
            if nums[mid] > nums[mid + 1]:
                return mid + 1 
            else:
                if nums[mid] >= nums[start]:
                    start = mid + 1 
                else:
                    end = mid - 1
        
        return 0
    
    def binary_search(self, nums, target, start, end):
        while start <= end:
            
            mid = (end + start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return -1 
                    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        pivot = self.find_pivot(nums)
        print(pivot)
        
        if nums[pivot] == target:
            return pivot
        # not rotated, normal binary search
        if pivot == 0:
            return self.binary_search(nums, target, 0, len(nums) - 1)
        
        # target is bigger than first number, then the target is somewhere right side
        if target < nums[0]:
            return self.binary_search(nums, target, pivot, len(nums) - 1)
        return self.binary_search(nums, target, 0, pivot) 