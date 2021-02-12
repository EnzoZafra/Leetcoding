class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        moves = [(0,1), (1,0), (-1,0), (0, -1)]
        rowLen = len(grid)
        colLen = len(grid[0])
        # should DFS/BFS and mark all the 1s as 0s.
        
        counter = 0
        
        for row in range(rowLen):
            for col in range(colLen):
                # we have an unvisited island
                if grid[row][col] == "1":
                    counter += 1
                    
                    # DFS to "visit" all parts of that island
                    stack = [(row, col)]
                
                    while stack:
                        curr = stack.pop()
                        currRow = curr[0]
                        currCol = curr[1]
                        grid[currRow][currCol] = "0"
                        
                        # visit neighbors
                        for move in moves:
                            dr = currRow + move[0]
                            dc = currCol + move[1]
                            
                            if dr >= 0 and dr < rowLen and dc >= 0 and dc < colLen and grid[dr][dc] == "1":
                                stack.append((dr, dc))

        return counter