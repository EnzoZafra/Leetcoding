# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def recur(node, lower_limit, upper_limit):
            if not node:
                return True
            
            if lower_limit > node.val or node.val > upper_limit:
                return False
            
            left = recur(node.left, lower_limit, node.val - 1)
            right = recur(node.right, node.val + 1, upper_limit)
            print(left, right)
            
            return left and right
        
        return recur(root, float('-inf'), float('inf'))