class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        inDegrees = collections.defaultdict(int)
        cities = set()
        
        for path in paths:
            source = path[0]
            dest = path[1]
            
            inDegrees[dest] += 1
            graph[source].append(dest)
            cities.add(source)
            cities.add(dest)
        
        zeroInDegrees = []
        for city in cities:
            if inDegrees[city] == 0:
                zeroInDegrees.append(city)
        
        while zeroInDegrees:
            curr = zeroInDegrees.pop()
            
            for neighbor in graph[curr]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    zeroInDegrees.append(neighbor)
        
        return curr