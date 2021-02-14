class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        
        for point in points:
            distance = math.sqrt(abs(0-point[0])**2 + abs(0-point[1]) ** 2)
            print(distance, point)
            heapq.heappush(heap, (distance, point)) 
        
        out = []
        for i in range(K):
            out.append(heappop(heap)[1]) 
        
        return out
