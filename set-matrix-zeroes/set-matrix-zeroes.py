class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroRows.add(row)
                    zeroCols.add(col)
                    
        for row in range(len(matrix)):
            if row in zeroRows:
                matrix[row] = [0 for _ in range(len(matrix[0]))]
                
            for col in range(len(matrix[0])):
                if col in zeroCols:
                    matrix[row][col] = 0
        
        return matrix