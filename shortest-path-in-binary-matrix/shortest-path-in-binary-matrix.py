class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1: 
            return -1
        
        rowLen = len(grid)
        colLen = len(grid[0])
        
        moves = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
        
        queue = deque() 
        queue.append((0,0,1))
        grid[0][0] = 1
        
        while queue:
            currRow, currCol, count = queue.popleft()
            if currRow == colLen - 1 and currCol == rowLen - 1:
                return count
            
            for move in moves:
                dr = currRow + move[0]
                dc = currCol + move[1]
                
                if 0 <= dr < rowLen and 0 <= dc < colLen and grid[dr][dc] == 0:
                    grid[dr][dc] = 1
                    queue.append((dr, dc, count+1))
        
        return -1
    
