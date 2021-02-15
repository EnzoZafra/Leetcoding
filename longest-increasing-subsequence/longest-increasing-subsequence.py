class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1 for _ in range(n)]
        out = 1
        
        for i in range(1, n):
            curr_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    # this would always get the best longest increasing subsequence so far
                    curr_max = max(curr_max, dp[j])
            
            # this would be 1 if there is no number nums[j] 0 <= j < i smaller than i 
            dp[i] = curr_max + 1
            out = max(out, dp[i])
        
        return out