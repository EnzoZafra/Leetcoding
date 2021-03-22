class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        
        for stick in sticks:
            heapq.heappush(heap, stick)
       
        totalcost = 0
        while len(heap) > 1:
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)
            
            cost = stick1 + stick2
            totalcost += cost
            heapq.heappush(heap, cost)
        
        return totalcost
        