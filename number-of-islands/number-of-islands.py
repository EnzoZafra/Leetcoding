class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def isValidMove(row, col):
            return 0 <= row < self.R and 0 <= col < self.C and grid[row][col] == "1"
        
        def dfs(row, col):
            stack = [(row,col)]
            
            while stack:
                currRow, currCol = stack.pop()
                grid[currRow][currCol] = "0"
                
                for move in self.moves:
                    dr = currRow + move[0]
                    dc = currCol + move[1]
                    
                    if isValidMove(dr,dc):
                        stack.append((dr,dc))
        
        self.R = len(grid)
        self.C = len(grid[0])
         
        self.moves = [(1,0), (0,1), (-1,0), (0,-1)]
        
        count = 0
        for row in range(self.R):
            for col in range(self.C):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        
        return count