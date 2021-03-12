# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parents = {}
        depths = collections.defaultdict(int)
        
        queue = deque()
        queue.append((root, 0, None))
        
        while queue:
            currNode, depth, parent = queue.popleft() 
            
            if currNode not in depths:
                depths[currNode.val] = depth
                parents[currNode.val] = parent
            
            if currNode.left:
                queue.append((currNode.left, depth+1, currNode))
                
            if currNode.right:
                queue.append((currNode.right, depth+1, currNode))
        
        
        if depths[x] == depths[y] and parents[x] != parents[y]:
            return True
        
        return False
        
            
            
            
            
        