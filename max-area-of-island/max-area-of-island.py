class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isValidMove(row, col):
            return 0 <= row < self.rowLen and 0 <= col < self.colLen
        
        def dfs(row, col):
            area = 0
            stack = [(row, col)]
            
            while stack:
                currRow, currCol = stack.pop()
                if (currRow, currCol) in self.visited:
                    continue
                
                area += 1
                self.visited.add((currRow, currCol))
                
                for move in self.moves:
                    dr = currRow + move[0]
                    dc = currCol + move[1]
                    
                    if isValidMove(dr, dc) and grid[dr][dc] == 1:
                        stack.append((dr,dc))
            
            return area
                    
        
        self.rowLen = len(grid)
        self.colLen = len(grid[0])
        
        maxArea = 0
        self.visited = set()
        self.moves = [(0,1), (1,0), (-1,0), (0,-1)]
        
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if grid[row][col] == 1: 
                    area = dfs(row, col)
                    maxArea = max(area, maxArea)
        
        return maxArea
                