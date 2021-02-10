class Solution(object):
    
    def fillLandAtBoundary(self, grid):
         # fill out the lands that is touching a boundary.
         # to do this, we start at the boundary and DFS to all connected 0s
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if at the boundary, DFS
                if (row == 0 or row == len(grid)-1 or col == 0 or col == len(grid[0])-1) and grid[row][col] == 0:
                    stack = [(row, col)]
                    while stack:
                        currRow, currCol = stack.pop()
                        grid[currRow][currCol] = 1
                        
                        for move in self.moves:
                            dr = currRow + move[0]
                            dc = currCol + move[1]
                            if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]) and grid[dr][dc] == 0:
                                stack.append((dr, dc)) 
        return grid
        
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # count the number of connected 0s instead of connected 1s
        
        # fill the 0s that are connected to the boundarys with 1
        
        self.moves = [(0,1), (1,0), (0,-1), (-1, 0)]
        grid = self.fillLandAtBoundary(grid)
        
        R = len(grid)
        C = len(grid[0])
        count = 0
        
        # loop for each point at the grid so that we can find multiple islands
        for row in range(R):
            for col in range(C):
                
                if grid[row][col] == 0:
                    # DFS from our starting point
                    stack = [(row, col)]

                    while stack:
                        curr = stack.pop()

                        # mark as 1 for visited
                        grid[curr[0]][curr[1]] = 1

                        for move in self.moves:
                            dr = curr[0] + move[0]
                            dc = curr[1] + move[1]

                            if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]) and grid[dr][dc] == 0:
                                stack.append((dr, dc)) 
                    count += 1
        return count