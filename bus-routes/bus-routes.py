class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # for each bus, get a map of what stop they can go to
        
        stopToRouteMap = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stopToRouteMap[stop].add(i)
        
        queue = deque([(source, 0)])
        visited = set([source])
        
        while queue:
            curr_stop, depth = queue.popleft()
            if curr_stop == target:
                return depth
            
            for route in stopToRouteMap[curr_stop]:
                for stop in routes[route]:
                    if stop not in visited:
                        queue.append((stop, depth + 1))
                        visited.add(stop)
                
                routes[route] = []
        
        return -1
            
                