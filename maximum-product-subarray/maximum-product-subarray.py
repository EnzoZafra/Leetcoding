class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        
        for i in range(1, len(nums)):
            num = nums[i] 
            
            # put in temp so we can calculate max_product 
            temp = min(max_product * num, min_product * num, num)
            max_product = max(max_product * num, min_product * num, num)
            
            min_product = temp
            
            result = max(max_product, result)
        
        return result
