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
           
            leftSum = max(recur(node.left), 0)
            rightSum = max(recur(node.right), 0)
            
            combined = leftSum + rightSum + node.val
            self.maxPathSum = max(combined, self.maxPathSum)
            
            return node.val + max(leftSum, rightSum)
        
        self.maxPathSum = float('-inf')
        recur(root)
        return self.maxPathSum