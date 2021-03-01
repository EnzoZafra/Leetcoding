# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def recur(arr, node, target):
            if not node:
                return
            
            arr.append(node.val)
            
            if target == node.val and not node.left and not node.right:
                self.out.append(arr[:])
            
            else:
                recur(arr, node.left, target - node.val) 
                recur(arr, node.right, target - node.val) 
                
            arr.pop()
                
            
        self.out = []
        recur([], root, targetSum)
        return self.out
                
            