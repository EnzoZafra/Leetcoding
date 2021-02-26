# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(arr, node):
            if not node:
                return
            
            inorder(arr, node.left)
            arr.append(node.val)
            inorder(arr, node.right)
        
        arr = []
        inorder(arr, root)
        
        return arr[k-1]