class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowLen = len(grid)
        colLen = len(grid[0])

        dp = [[float('inf') for _ in range(colLen)] for _ in range(rowLen)]

        # base cases 
        dp[0][0] = grid[0][0]

        for row in range(rowLen):
            for col in range(colLen):
                if (row, col) == (0, 0):
                    continue

                top = dp[row-1][col]
                left = dp[row][col-1]

                # we have a choice to come from top or left, take the minimum
                dp[row][col] = min(top, left) + grid[row][col]

        #print(dp)

        return dp[-1][-1]
        