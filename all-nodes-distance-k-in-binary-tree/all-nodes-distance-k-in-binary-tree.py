# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getParents(self, root):
        parents = {}
        parent = None
        
        queue = deque()
        queue.append((root, None))
        while queue:
            curr, parent = queue.popleft() 
            parents[curr] = parent
            
            if curr.left:
                queue.append((curr.left, curr))
                
            if curr.right:
                queue.append((curr.right, curr))
        
        return parents
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parents = self.getParents(root)
        
        # bfs from target 2 levels
        queue = deque()
        queue.append((target, 0))
        out = [] 
        visited = set()
        while queue:
            curr, level = queue.popleft()
            visited.add(curr)
            if level == K:
                out.append(curr.val)  
            
            if curr.left and curr.left not in visited:
                queue.append((curr.left, level+1))
                
            if curr.right and curr.right not in visited:
                queue.append((curr.right, level+1))
                
            if parents[curr] and parents[curr] not in visited:
                queue.append((parents[curr], level+1))
                
        return out
        
        
