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
        visited = {}
        
        stack = []
        stack.append(node)
        visited[node] = Node(node.val, [])
        while stack:
            curr = stack.pop()
                     
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
                
        return visited[node]
                     