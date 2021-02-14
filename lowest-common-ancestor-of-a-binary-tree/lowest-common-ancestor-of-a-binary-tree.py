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
        def recur(node, p, q):
            if not node:
                return 0
            
            if node == p or node == q:
                foundMid = 1
            else:
                foundMid = 0
            
            foundLeft = recur(node.left, p, q)
            foundRight = recur(node.right, p, q)
            
            if foundMid + foundLeft + foundRight >= 2:
                self.ans = node
            
            return foundMid or foundRight or foundLeft
        
        recur(root, p, q)
        return self.ans