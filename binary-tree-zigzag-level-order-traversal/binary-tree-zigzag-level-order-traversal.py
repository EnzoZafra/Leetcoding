# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        direction = False
        
        queue = deque()
        queue.append(root)
        
        out = []
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
            
            if direction:
                out.append(level[::-1])
            else:
                out.append(level)
                
            direction = not direction
    
        return out
                    