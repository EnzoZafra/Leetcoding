class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x,y in points:
            distance = sqrt((x**2 + y**2))
            print(x,y,distance)
            heapq.heappush(heap, (abs(distance), [x,y]))
        
        out = []
        while k > 0:
            k -= 1
            out.append(heapq.heappop(heap)[1])
        
        return out