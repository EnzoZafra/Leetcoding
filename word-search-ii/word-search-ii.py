class Solution(object):
    def findStartingLetters(self, words):
        startingLetterMap = collections.defaultdict(list)
        
        for word in words:
            startingLetterMap[word[0]].append(word)
        
        return startingLetterMap
    
    def isValidMove(self, row, col):
        return 0 <= row < self.rowLen and 0 <= col < self.colLen

    def dfs(self, board, word, row, col):
        start = ((row, col, 0)) 
        stack = [start]
        visited = set()
        
        while stack:
            currRow, currCol, currIndex = stack.pop()
            visited.add((currRow, currCol))
            
            if currIndex == len(word)-1:
                return True
            
            for move in self.moves:
                dr = currRow + move[0]
                dc = currCol + move[1]
                
                if self.isValidMove(dr, dc) and (dr,dc) not in visited and currIndex+1 < len(word) and board[dr][dc] == word[currIndex+1]:
                    stack.append((dr, dc, currIndex+1))
        
        return False
                
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:
            return []
        
        out = set()
        self.moves = [(1,0), (0,1), (-1,0), (0,-1)]
        startingLetterMap = self.findStartingLetters(words)
        
        self.rowLen = len(board)
        self.colLen = len(board[0])
        
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if board[row][col] in startingLetterMap:
                    for word in startingLetterMap[board[row][col]]:
                        # dfs and see if we can get the word
                        if self.dfs(board, word, row, col):
                            out.add(word)
        
        return out