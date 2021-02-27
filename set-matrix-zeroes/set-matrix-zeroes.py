class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])
        
        zero_cols = set()
        zero_rows = set()
        
        for row in range(rowLen):
            for col in range(colLen):
                if matrix[row][col] == 0:
                    zero_cols.add(col)
                    zero_rows.add(row)
                    
        for row in range(rowLen):
            if row in zero_rows:
                matrix[row] = [0 for _ in range(colLen)]
                continue
                
            for col in range(colLen):
                if col in zero_cols:
                    matrix[row][col] = 0
        
        return matrix
