class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.medianIndex = -1
        self.array = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.array:
            self.array.append(num)
        else:
            # find where to put via binary search
            index = bisect_left(self.array, num, 0, len(self.array)) 
            self.array.insert(index, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.array)
        if n % 2 == 1:
            return self.array[n/2]
        else:
            firstNum = float(self.array[(n/2) - 1])
            secondNum = float(self.array[n/2])
            return (firstNum + secondNum) / 2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()