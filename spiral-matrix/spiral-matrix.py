class Solution(object):
    def getNextPosition(self, r, c, direction):
        move = self.moves[direction] 
        dr = r + move[0]
        dc = c + move[1]

        return dr, dc
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # right, down, left, up continuously
        self.moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        rowLen = len(matrix)
        colLen = len(matrix[0])
        
        seen = set()
        ans = []
        r = 0
        c = 0
        direction = 0
        
        for _ in range(rowLen * colLen):
            ans.append(matrix[r][c])
            seen.add((r,c))
            
            dr, dc = self.getNextPosition(r, c, direction)
            
            if 0 <= dr < rowLen and 0 <= dc < colLen and (dr, dc) not in seen:
                r = dr
                c = dc
                
            # we hit a visited or we've hit a boundary
            else:
                direction = (direction + 1) % 4
                dr, dc = self.getNextPosition(r, c, direction)
                r = dr
                c = dc
        return ans
             
        