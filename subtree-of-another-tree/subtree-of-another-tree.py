# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def helper(x, y):
            if not x and not y:
                return True
            
            if not x or not y:
                return False
            
            return x.val == y.val and helper(x.left, y.left) and helper(x.right, y.right)
        
        def traverse(s, t):
            return (s and (helper(s,t) or traverse(s.left, t) or traverse(s.right,t)))
        
        return traverse(s,t)
