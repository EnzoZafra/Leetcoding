class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """

        dis = [[float('inf')] * n for _ in xrange(n)]
        
        for source, dest, weight in edges:
            dis[source][dest] = dis[dest][source] = weight
        
        # base case
        for i in range(n):
            dis[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        
            
        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in xrange(n)}
        return res[min(res)]
            
        
        