class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
                
        graph = collections.defaultdict(list)
        for source, dest, duration in times: 
            graph[source].append((dest, duration))
        
        
        maxTime = 0
        heap = []
        heapq.heappush(heap, (0, k))
        visited = set()
        visited.add(k)
        
        while heap:
            currTime, currNode = heapq.heappop(heap)
            if currNode not in visited:
                maxTime = currTime
                
            visited.add(currNode)
            
            for neighbor, duration in graph[currNode]:
                if neighbor not in visited:
                    heapq.heappush(heap, (duration+currTime, neighbor))
        
        return maxTime if len(visited) == n else -1