class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if len(jobDifficulty) < d:
            return -1
        
        # dp[i][d] = minimum difficulty schedule including jobs {1..i} spread out to d days.
        
        dp = [[float('inf') for _ in range(d)] for _ in range(len(jobDifficulty))]
        print(dp)
        
        # base case
        dp[0][0] = jobDifficulty[0]
        
        for i in range(1, len(jobDifficulty)):
            dp[i][0] = max(dp[i-1][0], jobDifficulty[i])
        
        for i in range(1, len(jobDifficulty)):
            for j in range(1, d):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + max(jobDifficulty[k+1:i+1]))
        
        return dp[-1][-1]