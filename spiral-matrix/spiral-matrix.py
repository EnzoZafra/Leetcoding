class Solution(object):
    def isInBounds(self, row, col, rowLen, colLen):
        return 0 <= row < rowLen and 0 <= col < colLen
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        rowLen = len(matrix)
        colLen = len(matrix[0])
        numItems = rowLen * colLen
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        directionIdx = 0
        
        visited = set()
        out = []
        
        curr = (0,0)
        
        for _ in range(numItems):
            currRow, currCol = curr
            out.append(matrix[currRow][currCol])
            visited.add(curr)
            
            nextmove = directions[directionIdx]
            dr = currRow + nextmove[0] 
            dc = currCol + nextmove[1]
            
            
            if not self.isInBounds(dr,dc,rowLen,colLen) or (dr, dc) in visited:
                directionIdx += 1
                directionIdx = directionIdx % 4
                
                nextmove = directions[directionIdx]
                dr = currRow + nextmove[0] 
                dc = currCol + nextmove[1]
                
            curr = (dr,dc)
            
                
        return out