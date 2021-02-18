# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # diameter = max distance from a left subtree to the right subtree (sibling)
        
        self.ans = 1
        
        def depth(node):
            if not node:
                return 0
             
            left = depth(node.left)
            right = depth(node.right)
            combined = left + right + 1
            
            self.ans = max(self.ans, combined)
            return max(left, right) + 1
        
        depth(root)
        return self.ans - 1