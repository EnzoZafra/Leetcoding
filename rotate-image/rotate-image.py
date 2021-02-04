class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
       
        # transpose
        for row in range(R):
            for col in range(row, C):
                tmp = matrix[col][row]
                matrix[col][row] = matrix[row][col]
                matrix[row][col] = tmp
        
        # reflect
        for row in range(R):
            for col in range(C/2):
                tmp = matrix[row][col]
                newCol = C - col - 1
                
                matrix[row][col] = matrix[row][newCol]
                matrix[row][newCol] = tmp
        
        print(matrix)
              
        
        
        