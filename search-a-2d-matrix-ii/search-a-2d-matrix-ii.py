class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rowLen = len(matrix)
        colLen = len(matrix[0])
        
        row = rowLen - 1
        col = 0
        
        while row >= 0 and col < colLen:
            curr = matrix[row][col]
            
            if target == curr:
                return True
            elif target > curr:
                col += 1
            else:
                row -= 1
        
        return False