class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        # valid tree means no cycle
        # topological sort

        graph = collections.defaultdict(list)
        
        for source, dest in edges:
            graph[source].append(dest)
            graph[dest].append(source)
        
        parent = {0:-1} 
        stack = [0]
        while stack:
            curr = stack.pop()
            
            for neighbor in graph[curr]:
                
                # dont go back to previous
                if neighbor == parent[curr]:
                    continue
                    
                # if we've seen it already 
                if neighbor in parent:
                    return False
                
                parent[neighbor] = curr
                stack.append(neighbor) 
                
        return len(parent) == n