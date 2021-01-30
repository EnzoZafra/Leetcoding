from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.loHeap = []
        self.hiHeap = []
    
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.loHeap) == len(self.hiHeap):
            heappush(self.hiHeap, -heappushpop(self.loHeap, -num))
        else:
            heappush(self.loHeap, -heappushpop(self.hiHeap, num))
            

    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.loHeap) == len(self.hiHeap):
            return float(self.hiHeap[0] - self.loHeap[0]) / 2.0
        else:
            return float(self.hiHeap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()