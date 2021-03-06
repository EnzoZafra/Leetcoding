class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        def dijkstras(graph, start):
            heap = [(0, start)]
            visited = set([start])
            neighbor = []
            
            while heap:
                dist, curr = heapq.heappop(heap)
                
                if curr not in visited:
                    neighbor.append(curr)
                
                visited.add(curr)
                
                for nextNeighbor, nextDistance in graph[curr]:
                    if nextNeighbor not in visited and nextDistance + dist <= distanceThreshold:
                        heapq.heappush(heap, (nextDistance + dist, nextNeighbor))
            
            return len(neighbor)
        
        
        graph = collections.defaultdict(list)
        for n1, n2, weight in edges:
            graph[n1].append((n2,weight))
            graph[n2].append((n1,weight))
        
        minNeighbors = float('inf')
        out = -1
        for i in range(n):
            neighborsLen = dijkstras(graph, i)
            
            if neighborsLen <= minNeighbors:
                minNeighbors = neighborsLen
                out = i
            
        return out 