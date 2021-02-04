class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_pivot(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                mid = (left + right) // 2

                # if not sorted, we found the pivot
                if nums[mid+1] < nums[mid]:
                    return mid + 1
                else:
                    # check if the first item is still smaller than mid
                    if nums[left] <= nums[mid]:
                        left = mid + 1 
                    else:
                        right = mid - 1
                        
            return -1
                

        
        def bst(start, end):
            while start <= end:
                mid = (end + start) // 2

                # target is lower than mid number
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    return mid

            return -1
        
        if not nums:
            return -1
        
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        
        # bst to find the pivot point
        pivot = find_pivot(0, len(nums) - 1)
        print(pivot)
        
        if nums[pivot] == target:
            return pivot
        
        # if not rotated, BST all
        if pivot == 0:
            return bst(0, len(nums) - 1)
        
        # if target is greater than the first item, that means search the left half
        if target > nums[0]:
            return bst(0, pivot)
        elif target < nums[0]:
            return bst(pivot, len(nums)-1)
        else:
            return 0
        
        return -1
        
        
        
        
        
