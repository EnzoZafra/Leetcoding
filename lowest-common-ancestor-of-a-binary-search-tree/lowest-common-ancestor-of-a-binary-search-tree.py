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
        if not root:
            return None
        
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        
        # in left subtree
        if p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # in right subtree
        elif p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root
