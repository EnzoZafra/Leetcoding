class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        
        # merge the two sorted arrays, then get the middle number?
        index1 = 0
        index2 = 0
        
        while index1 < len(nums1) and index2 < len(nums2):
            num1 = nums1[index1]     
            num2 = nums2[index2]
            
            if num1 <= num2:
                merged.append(num1)
                index1 += 1
            else:
                merged.append(num2)
                index2 += 1
        
        if index1 < len(nums1):
            merged = merged + nums1[index1:]
        else:
            merged = merged + nums2[index2:]
        
        length = len(merged)
        if length % 2 == 0:
            # if even, we need to take the average of middle two numbers
            mid = int(floor(length/2))
            return (merged[mid-1] + merged[mid])/ float(2)
        else:
            mid = int(ceil(length/2))
            return (merged[mid]) 
        
        
        