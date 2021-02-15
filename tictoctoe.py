# Tic Toc Toe game
# 1. create a class to represent a game of tic toc toe
# 2. create a function to check if there is a valid winning score
# 3. create a function to return all possible game states given a board
# 4. create a function to predict the next best move for an AI
from enum import Enum

class TicTocToeCellTypes(Enum):
    X = 'X',
    O = 'O'
    

class TicTocToeCell(object):
    def __init__(self, tictoctoe_type=None):
        self._is_filled = False
        self._type = tictoctoe_type
    
    def isValidMove(self):
        return not self._is_filled
    
    def populate_cell(self, tictoctoe_type):
        self._type = tictoctoe_type
        self._is_filled = True
    
    def remove_cell(self):
        self._type = None
        self._is_filled = False
    
    def __repr__(self):
        return self._type.value[0] if self._is_filled else ' '

class TicTocToeBoard(object):
    def __init__(self, rowLen=3, colLen=3):
        self.rowLen = rowLen
        self.colLen = colLen
        self.grid = [[TicTocToeCell() for _ in range(rowLen)] for _ in range(rowLen)]
    
    def print_grid(self):
        print(' ')
        for row in self.grid:
            print(row)
    
    def deep_copy(self):
        copy = TicTocToeBoard(self.rowLen, self.colLen)
        
        for row in range(self.rowLen):
            for col in range(self.colLen):
                cell_to_copy = self.grid[row][col]
                if cell_to_copy._is_filled:
                    copied_cell = copy.grid[row][col]
                    copied_cell.populate_cell(cell_to_copy._type)
                    
        return copy
    
    def populate_cell(self, row, col, tictoctoe_type):
        cell = self.grid[row][col]
        
        if cell.isValidMove():
            cell.populate_cell(tictoctoe_type)
            return True
        else:
            print('That cell is already populated')
            return False
    
    def is_out_of_bounds(self, row, col):
        if row >= 0 and col >= 0 and row < self.rowLen and col < self.colLen:
            return False
        
        return True
    
    def all_populated(self):
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if self.grid[row][col].isValidMove():
                    return False
        
        return True
    
    def get_non_populated_cells(self):
        out = []
        for row in range(self.rowLen):
            for col in range(self.colLen):
                cell = self.grid[row][col]
                if cell.isValidMove():
                    out.append((row,col))
                    
        return out
    
    
    # was used to check for winner, but dont need this anymore
    def _dfs(self, row, col, type_wanted):
        moves = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1)]
        
        stack = [(row, col)]
        consecutive_counter = 0 
        visited = set()
        
        while stack:
            currRow, currCol = stack.pop()
            visited.add((currRow, currCol))
            
            consecutive_counter += 1
            
            if consecutive_counter == 3:
                return True
            
            for move in moves:
                dr = currRow + move[0]
                dc = currCol + move[1]
                
                if not self.is_out_of_bounds(dr, dc) and (dr,dc) not in visited:
                    cell = self.grid[dr][dc]
                    if cell._type == type_wanted:
                        stack.append((dr,dc))         
                    
        return False
    
    def _check_consecutive_array(self, array):
        toCheck = array[0]
        if toCheck.isValidMove():
            return False
        
        
        for elem in array[1:]:
            if elem._type != toCheck._type:
                return False
        
        return True
    
    def get_list_cols(self):
        out = []
        
        for col in range(self.colLen):
            new_col = []
            for row in range(self.rowLen):
                new_col.append(self.grid[row][col])
            
            out.append(new_col)
        return out
    
    
    def calculate_if_winner(self):
        # check rows:
        for rowIndex, row in enumerate(self.grid):
            if self._check_consecutive_array(row):
                cell = self.grid[rowIndex][0]
                print(cell._type.value[0] + " WINS!")
                return True
        
        for colIndex, col in enumerate(self.get_list_cols()):
            if self._check_consecutive_array(col):
                cell = self.grid[0][colIndex]
                print(cell._type.value[0] + " WINS!")
                return True

        print('no winner')
        return False
    
    def calculate_next_possible_moves(self, next_move):
        # backtracking
        def backtrack(out, curr_grid, next_move):
            if curr_grid.all_populated():
                out.append(curr_grid)
            
            for row,col in curr_grid.get_non_populated_cells():
                copy = curr_grid.deep_copy()
                cell = copy.grid[row][col]
                cell.populate_cell(next_move)
                backtrack(out, copy, TicTocToeCellTypes.X if next_move == TicTocToeCellTypes.O else TicTocToeCellTypes.O)
                cell.remove_cell
        
        out = []
        backtrack(out, self, next_move)
        
        return out
                

    
    
game = TicTocToeBoard()


game.populate_cell(0,0,TicTocToeCellTypes.X)
game.populate_cell(0,1,TicTocToeCellTypes.X)
game.populate_cell(0,2,TicTocToeCellTypes.O)

game.populate_cell(1,0,TicTocToeCellTypes.O)
game.populate_cell(1,1,TicTocToeCellTypes.X)
game.populate_cell(1,2,TicTocToeCellTypes.O)

game.populate_cell(2,0,TicTocToeCellTypes.O)


game.print_grid()

winner = game.calculate_if_winner()

possibleStates = game.calculate_next_possible_moves(TicTocToeCellTypes.X)

# printing possible states
for states in possibleStates:
    states.print_grid()
