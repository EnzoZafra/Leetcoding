class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        rowLen = len(matrix)
        colLen = len(matrix[0])
        
        dp = [[0 for _ in range(colLen+1)] for _ in range(rowLen+1)]
        maxSide = 0
        
        for row in range(1, rowLen+1):
            for col in range(1, colLen+1):
                if matrix[row-1][col-1] == "1":
                    left = dp[row][col-1]
                    up = dp[row-1][col]
                    topleft = dp[row-1][col-1]

                    dp[row][col] = min(left, up, topleft) + 1
                    maxSide = max(dp[row][col], maxSide)
        print(dp) 
        return maxSide ** 2
