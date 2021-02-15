# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def recur(left_inorder, right_inorder):
            if left_inorder == right_inorder:
                return None
            
            root_val = preorder[self.preorderIndex]

            index = self.inOrderIndex[root_val]

            self.preorderIndex += 1
            root = TreeNode(root_val, recur(left_inorder, index), recur(index+1, right_inorder))

            return root

        self.preorderIndex = 0 
        self.inOrderIndex = {nodeValue : index for index, nodeValue in enumerate(inorder)}

        root = recur(0, len(inorder))
        return root