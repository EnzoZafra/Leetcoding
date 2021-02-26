class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def backtrack(origin, route):
            if len(route) == len(tickets) + 1:
                self.out = route
                return True
            
            for i, nextDest in enumerate(self.graph[origin]):
                if not self.visited[origin][i]:
                    self.visited[origin][i] = True
                    if backtrack(nextDest, route + [nextDest]):
                        return True
                    self.visited[origin][i] = False
            
            return False
        
        self.graph = collections.defaultdict(list)
        self.visited = {}
        
        for ticket in tickets:
            source = ticket[0]
            dest = ticket[1]
            
            self.graph[source].append(dest)
            
        for source in self.graph:
            neighbors = self.graph[source]
            neighbors.sort()
            self.visited[source] = [False for _ in range(len(neighbors))]
        
        self.out = []
        flights = len(tickets)
        route = ['JFK']
        backtrack('JFK', route)
        
        return self.out
