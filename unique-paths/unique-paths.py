class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # base case, left column and top row should be 1
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for row in range(1,m):
            for col in range(1,n):
                # choice is coming from the top plus coming from the left
                left = dp[row][col-1]
                top = dp[row-1][col]
                dp[row][col] = left + top
        
        return dp[m-1][n-1]
                
        
        
        