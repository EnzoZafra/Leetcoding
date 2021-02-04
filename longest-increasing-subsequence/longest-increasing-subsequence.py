class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = [1 for _ in range(len(nums))]

        maxSoFar = 1
        for i in range(1, len(nums)):
            maxval = 0
            
            # inner loop
            for j in range(0, i):
                # if increasing, we add to the previous longest subsequence up to i 
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
                    
            dp[i] = maxval + 1
            maxSoFar = max(maxSoFar, dp[i])
       
        return maxSoFar
        