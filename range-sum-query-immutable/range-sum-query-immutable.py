class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return

        self.prefixSums = [0 for _ in range(len(nums))]
        
        self.prefixSums[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefixSums[i] = nums[i] + self.prefixSums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.prefixSums[j]
        
        return self.prefixSums[j] - self.prefixSums[i-1]
                       
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)