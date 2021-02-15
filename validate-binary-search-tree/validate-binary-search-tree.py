# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # do an inorder traversal, check that strictly increasing
        stack = []
        prev = None
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # visit:
            curr = stack.pop()
            if prev and prev.val >= curr.val:
                return False
            
            prev = curr
            curr = curr.right
       
        return True
            
        
