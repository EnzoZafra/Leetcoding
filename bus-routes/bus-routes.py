class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        to_routes = collections.defaultdict(set)
        
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
                
        print(to_routes)
        
        queue = deque()
        queue.append((source, 0))
        
        seen = set([source])
        while queue:
            busNumber, bussesTaken = queue.popleft()
            if busNumber == target: 
                return bussesTaken
            
            #print(busNumber, to_routes[busNumber])
            
            # get the bus stops that the bus number goes to
            for i in to_routes[busNumber]:
                
                # for each bus in this bus stop
                #print(routes[i])
                for j in routes[i]:
                    
                    # take the bus and see if we end up at the target
                    if j not in seen:
                        queue.append((j, bussesTaken + 1))
                        #print(j, bussesTaken+1)
                        seen.add(j)
                        
                routes[i] = []  # seen route
        return -1