class Solution(object):
    
    def isValidMove(self, row, col):
        return 0 <= row < self.rowLen and 0 <= col < self.colLen
    
    def dfs(self, matrix, row, col, visited):
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        
        stack = []
        stack.append((row, col, matrix[row][col]))
        
        while stack:
            currRow, currCol, startingHeight = stack.pop()
            visited.add((currRow, currCol))
            
            for move in moves:
                dr = currRow + move[0]
                dc = currCol + move[1]
                
                if self.isValidMove(dr, dc) and (dr,dc) not in visited and startingHeight <= matrix[dr][dc]:
                    stack.append((dr,dc, matrix[dr][dc]))
        
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        
        self.rowLen = len(matrix)
        self.colLen = len(matrix[0])
        
        self.atlantic = set()
        self.pacific = set()
        
        # start from atlantic and pacific edges
        # mark all the nodes that is visitable
        for col in range(self.colLen):
            self.dfs(matrix, self.rowLen-1, col, self.atlantic)
            self.dfs(matrix, 0, col, self.pacific)
            
        for row in range(self.rowLen):
            self.dfs(matrix, row, self.colLen-1, self.atlantic)
            self.dfs(matrix, row, 0, self.pacific)
        
        out = []
        for coordinates in self.atlantic:
            if coordinates in self.pacific:
                out.append(coordinates)
        
        return out
                
                