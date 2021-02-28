class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for col in range(n):
            dp[0][col] = 1
            
        for row in range(m):
            dp[row][0] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                left = dp[row][col-1]
                up = dp[row-1][col]
                dp[row][col] = up + left
        print(dp)
        return dp[-1][-1]
        
        