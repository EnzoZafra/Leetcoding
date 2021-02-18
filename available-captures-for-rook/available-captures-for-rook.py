class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rowLen = len(board)
        colLen = len(board[0])
        rook = None
        
        # find the white rook first on the chess board
        for row in range(rowLen):
            for col in range(colLen):
                if board[row][col] == 'R':
                    rook = (row, col)
                    break
        
        # now that we have the rook, do the moves, and count how many times we can kill
        # that is, just see if theres a black that is not blocked by a white
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        count = 0
        
        for direction in directions:
            x = rook[0] + direction[0]
            y = rook[1] + direction[1]
            while 0 <= x < rowLen and 0 <= y < colLen:
                piece = board[x][y]
                
                if piece == 'p':
                    count += 1
                    break
                elif piece.isupper():
                    # if a white piece, we cant check this direction anymore
                    break
                
                x = x + direction[0]
                y = y + direction[1]
        
        return count
                    
        