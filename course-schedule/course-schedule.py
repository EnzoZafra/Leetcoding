class Solution:
    def build_adjacency_graph_indegrees(self, numCourses, prerequisites):
        graph = {x:[] for x in range(numCourses)}
        indegrees = {x:0 for x in range(numCourses)}
        
        for prereq in prerequisites:
            source = prereq[1]
            dest = prereq[0]
            
            graph[source].append(dest)
            indegrees[dest] += 1
            
        return graph, indegrees
    
    def get_zero_indegrees(self, indegrees):
        zero_indegrees = []
        
        for courseNum, indegree in indegrees.items():
            if indegree == 0:
                zero_indegrees.append(courseNum)
        
        return zero_indegrees
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
                
        graph, indegrees = self.build_adjacency_graph_indegrees(numCourses, prerequisites)
        zeroInDegrees = self.get_zero_indegrees(indegrees)
        
        sortedOrder = []
        while zeroInDegrees:
            curr = zeroInDegrees.pop()
            sortedOrder.append(curr) 
            
            for neighbor in graph[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zeroInDegrees.append(neighbor)
                    
        return True if len(sortedOrder) == numCourses else False
           
             