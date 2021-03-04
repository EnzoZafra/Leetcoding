"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def generate_copies(node):
            copyMap = {}

            stack = [node]
            visited = set(stack)
            while stack:
                curr = stack.pop()
                
                copy = Node(curr.val)
                copyMap[curr.val] = copy

                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            
            return copyMap
        
        def populate_neighbors(node, copyMap):
            stack = [node]
            visited = set(stack)
            while stack:
                curr = stack.pop()
                
                copy = copyMap[curr.val]
                
                for neighbor in curr.neighbors:
                    neighborCopy = copyMap[neighbor.val]
                    copy.neighbors.append(neighborCopy)
                    
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        stack.append(neighbor)
            
            return copyMap[node.val]
        
        if not node:
            return None
        
        copyMap = generate_copies(node)
        copyRoot = populate_neighbors(node, copyMap)
        return copyRoot
                    
            