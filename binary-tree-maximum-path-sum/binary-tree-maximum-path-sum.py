# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        def recur(node):
            if not node:
                return 0

            # leaf 

            left = max(recur(node.left), 0)
            right = max(recur(node.right), 0)

            # we should either return the new tree, or old tree + extra path
            newTree = node.val + left + right

            self.max = max(self.max, newTree)

            return node.val + max(left, right)
        
        self.max = float('-inf')
        recur(root)
        
        return self.max
        