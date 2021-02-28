class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(row, col, word):
            if len(word) == 0:
                return True
            
            for move in self.moves:
                dr = row + move[0]
                dc = col + move[1]
                
                if 0 <= dr < self.rowLen and 0 <= dc < self.colLen and board[dr][dc] == word[0]:
                    board[dr][dc] = '#'
                    if dfs(dr, dc, word[1:]):
                        return True
                    board[dr][dc] = word[0]

            return False 
        
        self.rowLen = len(board)
        self.colLen = len(board[0])
        
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if board[row][col] == word[0]:
                    board[row][col] = '#'
                    
                    if dfs(row, col, word[1:]):
                        return True
                    
                    board[row][col] = word[0]
        
        return False