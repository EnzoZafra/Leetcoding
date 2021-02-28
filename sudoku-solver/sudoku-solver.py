from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            rows[row].add(d)
            columns[col].add(d)
            boxes[box_index(row, col)].add(d)
            
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            rows[row].remove(d)
            columns[col].remove(d)
            boxes[box_index(row, col)].remove(d)
            
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            # if we're in the last cell
            # that means we have the solution
            
            if col == N - 1 and row == N - 1:
                self.sudoku_solved = True
            
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                    
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        
                        if not self.sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        n = 3
        N = len(board)
        
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [set() for i in range(N)]
        columns = [set() for i in range(N)]
        boxes = [set() for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        self.sudoku_solved = False
        backtrack()
