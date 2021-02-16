class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        print(dp)
        
        # base case, populate top row and leftmost column by 1
        for row in range(m):
            dp[row][0] = 1
        
        for col in range(n):
            dp[0][col] = 1
            
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[-1][-1]
        