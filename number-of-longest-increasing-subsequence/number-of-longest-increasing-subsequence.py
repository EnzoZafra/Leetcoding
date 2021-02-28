class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [[1,1] for _ in range(len(nums))]
        longest = 1
        
        for i in range(len(nums)):
            curr_longest = 1
            count = 0
            
            for j in range(i):
                
                # if increasing, we can add to the old count
                if nums[j] < nums[i]:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            
            # counting step
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < nums[i]:
                    count += dp[j][1]
            
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
                
        return sum([item[1] for item in dp if item[0] == longest])
            
        