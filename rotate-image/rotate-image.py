class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # to rotate, we have to reflect then transpost
        
        
        rowLen = len(matrix)
        colLen = len(matrix[0])
        
        # reflect
        
        start = 0
        end = rowLen - 1
        while start < end:
            temp = matrix[end] 
            matrix[end] = matrix[start]
            matrix[start] = temp
            
            start += 1
            end -= 1
        
        # transpose
        for row in range(rowLen):
            for col in range(row, colLen):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        print(matrix) 

        return matrix
    
