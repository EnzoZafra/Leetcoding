class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # max heap
        self.lo = []
        
        # min heap
        self.hi = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -1 * num)
        
        # rebalance
        popped = -1 * heapq.heappop(self.lo)
        heapq.heappush(self.hi, popped)
        
        if len(self.lo) < len(self.hi):
            popped = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -1 * popped)

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-1 * self.lo[0])
        else:
            return float(self.hi[0] - self.lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()