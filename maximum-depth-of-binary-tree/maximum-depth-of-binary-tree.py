# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque()
        depth = 1
        queue.append((root, depth))
        
        while queue:
            curr, depth = queue.popleft()
            
            if curr.left:
                queue.append((curr.left, depth + 1))
                
            if curr.right:
                queue.append((curr.right, depth + 1))
        
        return depth
        