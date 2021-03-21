class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def checkRot(row, col):
            for move in self.moves:
                dr = row + move[0]
                dc = col + move[1]
                
                if 0 <= dr < self.R and 0 <= dc < self.C:
                    if grid[dr][dc] == 2:
                        return 2
            
            return 1
        
        def countFresh():
            countFresh = 0
            for row in range(self.R):
                for col in range(self.C):
                    if grid[row][col] == 1:
                        countFresh += 1
            
            return countFresh
        
        def processMinute(grid):
            gridcopy = [[0 for _ in range(self.C)] for _ in range (self.R)]
            somethingHappened = False
            freshCount = 0
            
            for row in range(self.R):
                for col in range(self.C):
                    orange = grid[row][col]
                    
                    if orange == 1:
                        test = checkRot(row, col)
                        if test == 2:
                            somethingHappened = True
                        else:
                            freshCount += 1
                            
                        gridcopy[row][col] = test
                    else:
                        gridcopy[row][col] = orange
            
            return gridcopy, somethingHappened, freshCount
        
        
        self.moves = [(0,1), (1,0), (0,-1), (-1,0)]
        self.R = len(grid)
        self.C = len(grid[0])
        
        countFresh = countFresh()
        if countFresh == 0:
            return 0
        
        minute = 0
        
        while True:
            grid, somethingHappened, freshCount = processMinute(grid)
            if not somethingHappened:
                if freshCount == 0:
                    return minute
                else:
                    return -1
            else:
                minute += 1
            