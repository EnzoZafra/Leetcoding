# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rowLen, colLen = binaryMatrix.dimensions()
        
        earliestIndex = float('inf')
        for row in range(rowLen):
            # BST
            start = 0
            end = colLen - 1
            
            while start < end:
                mid = (end + start) // 2

                if binaryMatrix.get(row, mid) == 1:
                    end = mid
                else:
                    start = mid+1
            
            
            if binaryMatrix.get(row, start) == 1:
                earliestIndex = min(earliestIndex, start)
                    
        return earliestIndex if earliestIndex != float('inf') else -1