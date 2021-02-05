# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        self.ans = None
        
        def recur(node):
            if not node:
                return False

            # need to recur
            left = recur(node.left)
            right = recur(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                self.ans = node

            return mid or left or right
        
        recur(root)
        
        return self.ans
                    
         
            
        
        