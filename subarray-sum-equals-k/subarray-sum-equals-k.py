class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefixSum = 0
        
        previousSums = {}
        previousSums[0] = 1
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            diff = prefixSum - k
            
            if diff in previousSums:
                count += previousSums[diff]
            
            previousSums[prefixSum] = previousSums.get(prefixSum, 0) + 1

        return count