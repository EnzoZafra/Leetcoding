class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        
        maxSum = dp[0]
        for i in range(1, len(nums)):
            # Choice, include to our subarray, or start a new one
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            maxSum = max(maxSum, dp[i])
        
        return maxSum