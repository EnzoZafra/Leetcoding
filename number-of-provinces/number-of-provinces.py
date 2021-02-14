class Solution(object):
    def build_adjacency_graph(self, isConnected):
        graph = collections.defaultdict(set)
        
        for sourceIdx, connectedInfo in enumerate(isConnected):
            for destIdx, node in enumerate(connectedInfo):
                if node == 1 and destIdx != sourceIdx:
                    graph[sourceIdx+1].add(destIdx+1)
        
        return graph
        
    def dfs(self, node, visited, graph):
        stack = [node]
        while stack:
            curr = stack.pop()
            visited.add(curr)
            
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        # 1. preprocess isConnected array to build graph of neighbors
        # 2. loop through all nodes
        # 3. if not visited, start DFS
        # 4. in DFS, visit all the neighbors mark them as visited
        # 5. When DFS is done, increment province counter
        # 6. if not all nodes visited, go back to STEP 2
        
        
        # 1. preprocess isConnected array to build graph
        graph = self.build_adjacency_graph(isConnected)
        
        visited = set()
        counter = 0
        for i in range(len(isConnected)):
            node = i+1
            if node not in visited:
                self.dfs(node, visited, graph)
                counter += 1
        
        return counter