# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def recur(current, parent, grandparent):
            if not current:
                return
            
            if grandparent and grandparent.val % 2 == 0:
                self.sum += current.val
            
            recur(current.left, current, parent)
            recur(current.right, current, parent)
        
        self.sum = 0
        recur(root, None, None)
        return self.sum 
