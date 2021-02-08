class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        starter = collections.defaultdict(list)
        for word in words:
            starter[word[0]].append(word)
        
        R = len(board)
        C = len(board[0])
        moves = [(0,1), (1, 0), (0, -1), (-1, 0)]
        out = set()
        
        for row in range(R):
            for col in range(C):
                char = board[row][col]
                
                if char in starter:
                    possibleWords = starter[char]
                    for temp in possibleWords:
                        # DFS
                        stack = []
                        possibleWord = temp[1:]
                        stack.append((row, col, temp[1:]))
                        visited = set()
                        while stack:
                            currRow, currCol, possibleWord = stack.pop() 
                            visited.add((currRow, currCol))
                            if possibleWord == '':
                                out.add(temp)
                                break
                                
                            for move in moves:
                                dr = currRow + move[0]
                                dc = currCol + move[1]

                                if dr >= 0 and dc >= 0 and dr < R and dc < C and (dr, dc) not in visited and board[dr][dc] == possibleWord[0]:
                                    stack.append((dr, dc, possibleWord[1:]))
                                    
        return out