class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose then reflect
        
        R = len(matrix)
        C = len(matrix[0])
        
        def transpose(matrix):
            for row in range(R):
                for col in range(row, R):
                    matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        
        def reflect(matrix):
            for row in range(R):
                for col in range(C // 2):
                    matrix[row][col], matrix[row][C-col-1] = matrix[row][C-col-1], matrix[row][col]
                    
        
        transpose(matrix)
        reflect(matrix)
        print(matrix)
      
        
        
        