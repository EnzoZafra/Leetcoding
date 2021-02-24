# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def recur(node):
            if not node:
                return None
            
            right = recur(node.right)
            left = recur(node.left)
            
            node.left = right
            node.right = left
            
            return node
        
        recur(root)
        return root