class Solution(object):
        
    def isInGrid(self, rowLen, colLen, dr, dc):
        return 0 <= dr < rowLen and 0 <= dc < colLen
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # bfs. only proceed to a child, if the value of the child is the next letter we want to visit.
        # keep a visited set so since we can use the same cell more than once
        
        if not board or not word:
            return None

        # we need to backtrack because sometimes, we should be taking a different way
        self.moves = [(0,1), (1,0), (-1,0), (0,-1)]
        self.rowLen = len(board)
        self.colLen = len(board[0])
        
        def bfs(row, col, curr_word):
            # base case, we've completed our word
            if len(curr_word) == 0:
                return True
            
            for move in self.moves:
                dr = row + move[0]
                dc = col + move[1]
                # if the neighbor is not out of bounds and its the letter we need, take the move
                if self.isInGrid(self.rowLen, self.colLen, dr, dc) and board[dr][dc] == curr_word[0] and (dr, dc) not in self.seen:
                    self.seen.add((dr, dc))
                    if bfs(dr, dc, curr_word[1:]):
                        return True
                    self.seen.remove((dr, dc))
                    
            return False
                    
       
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if board[row][col] == word[0]:
                    self.seen = set()
                    self.seen.add((row, col))
                    if bfs(row,col,word[1:]):
                        return True
                    
        return False
        
    
        
        
        
        