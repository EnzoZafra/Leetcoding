import heapq

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        return self.dijkstras(n, edges, distanceThreshold) 
        
    def floyd(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type dptanceThreshold: int
        :rtype: int
        """

        dp = [[float('inf')] * n for _ in xrange(n)]
        
        for source, dest, weight in edges:
            dp[source][dest] = weight
            dp[dest][source] = weight
        
        # base case
        for i in range(n):
            dp[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
            
        res = {sum(d <= distanceThreshold for d in dp[i]): i for i in xrange(n)}
        return res[min(res)]
    
    def dijkstras(self, n, edges, distanceThreshold):
        
        graph = collections.defaultdict(list)
        for source, dest, weight in edges:
            graph[dest].append((source,weight))
            graph[source].append((dest,weight))
         
        neighbors = {}
        minNeighborNode = -1
        minNeighbors = float('inf')
        
        for node in range(n):
            heap = [(0, node)]
            visited = set([node])
            neighbor = []
            
            while heap:
                dist, curr = heapq.heappop(heap)
                
                if curr not in visited:
                    neighbor.append(curr)  
                    
                visited.add(curr)
                for nextNeighbor, nextDistance in graph[curr]:
                    if nextNeighbor not in visited and distanceThreshold >= dist+nextDistance:
                        heapq.heappush(heap, (dist+nextDistance, nextNeighbor))
            
            length = len(neighbor)
            neighbors[node] = neighbor
            if minNeighbors >= length:
                minNeighbors = length
                
                minNeighborNode = node
        print(neighbors)    
        return minNeighborNode
                
        
        