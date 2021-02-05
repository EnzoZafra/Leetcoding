class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        if not numCourses:
            return []
        
        
        # topological sort problem
        
        inDegrees = {x:0 for x in range(numCourses)}
        graph = {x:[] for x in range(numCourses)}
        
        for prereq in prerequisites:
            dest = prereq[0]
            source = prereq[1]
            
            inDegrees[dest] += 1
            graph.get(source).append(dest)
            
        zeroInDegrees = []
        for key, val in inDegrees.items():
            if val == 0:
                zeroInDegrees.append(key)
        
        # now we can do a DFS
        out = []
        while zeroInDegrees:
            curr = zeroInDegrees.pop()
            out.append(curr) 
            neighbors = graph.get(curr)
            
            for neighbor in neighbors:
                # decrease their indegree 
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    zeroInDegrees.append(neighbor)
        
        return out if len(out) == numCourses else []
            
