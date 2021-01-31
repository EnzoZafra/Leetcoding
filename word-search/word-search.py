class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        self.R = len(board)
        self.C = len(board[0])
        self.directions = [(0,1), (1,0), (-1, 0), (0, -1)]

        def backtrack(row, col, path):
            if len(path) == 0:
                return True
            
            # if it is not the correct letter or out of bounds, no need to proceed
            if row < 0 or col < 0 or row >= self.R or col >= self.C or board[row][col] != path[0]:
                return False
            
            # mark visited
            board[row][col] = '#'
            
            for direction in self.directions:
                dr = row + direction[0]
                dc = col + direction[1]
                
                if backtrack(dr, dc, path[1:]):
                    return True
                
            # backtrack the mark
            board[row][col] = path[0]
            
            return False
        
        for row in range(self.R):
            for col in range(self.C):
                if backtrack(row, col, word):
                    return True
        
        return False