"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        root_clone = Node(node.val)

        queue = deque()
        queue.append(node)
        
        visited = {}
        visited[node] = root_clone
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    cloneNeighbor = Node(neighbor.val)
                    visited[neighbor] = cloneNeighbor
                    queue.append(neighbor)
                    
                visited[curr].neighbors.append(visited[neighbor])
                
        return visited[node]
                