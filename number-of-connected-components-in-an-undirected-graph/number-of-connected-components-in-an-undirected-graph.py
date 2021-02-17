class Solution(object):
    def get_adjacency_map(self, n, edges):
        graph = {x:[] for x in range(n)} 
        for edge in edges:
            source = edge[0]
            dest = edge[1]
            graph[source].append(dest)
            graph[dest].append(source)
        
        return graph
    
    def dfs(self, visited, start, graph):
        stack = [start]

        while stack:
            curr = stack.pop()
            visited.add(curr)

            for neighbor in graph[curr]:
                print(neighbor)
                if neighbor not in visited:
                    stack.append(neighbor)
        
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n == 0:
            return 0

        graph = self.get_adjacency_map(n, edges) 
        
        count = 0
        visited = set()
        
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(visited, i, graph)
        return count