"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def findroot(node):
            if not node.parent:
                return node
            
            return findroot(node.parent)
        
        def recur(node):
            if not node:
                return False
            
            mid = node == p or node == q
            left = recur(node.left)
            right = recur(node.right)
            
            if mid + left + right >= 2:
                self.out = node
            
            return left or right or mid
        
        root = findroot(p)
        self.out = None
        recur(root)
        
        return self.out
        