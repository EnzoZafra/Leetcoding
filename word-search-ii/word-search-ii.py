class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        starts = collections.defaultdict(set)
        
        for word in words:
            starts[word[0]].add(word)
        
        R = len(board)
        C = len(board[0])
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        
        out = set()
        for row in range(R):
            for col in range(C):
                starting_char = board[row][col]
                
                if starting_char in starts:
                    for word in starts[starting_char]:
                        visited = set([(row,col)])
                        stack = [(row, col, word[1:])]

                        while stack:
                            currRow, currCol, currWord = stack.pop()
                            visited.add((currRow,currCol))
                            
                            if not currWord:
                                out.add(word)
                                break

                            for move in moves:
                                dr = currRow + move[0]
                                dc = currCol + move[1]

                                if 0 <= dr < R and 0 <= dc < C and board[dr][dc] == currWord[0] and (dr,dc) not in visited:
                                    stack.append((dr,dc,currWord[1:]))
        
        return out
