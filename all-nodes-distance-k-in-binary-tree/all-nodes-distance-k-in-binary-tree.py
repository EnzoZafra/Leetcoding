# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parents = {}
        
        stack = [(root, None)]
        while stack:
            currNode, parent = stack.pop() 
            parents[currNode] = parent
            
            if currNode.left:
                stack.append((currNode.left, currNode))
                
            if currNode.right:
                stack.append((currNode.right, currNode))
        
        
            
        queue = deque()
        queue.append((target, 0))
        
        out = []
        visited = set([target])
        while queue:
            curr, dist = queue.popleft()
            visited.add(curr)
            
            if dist == K:
                out.append(curr.val)
            elif dist > K:
                return out
        
            if curr.left and curr.left not in visited:
                queue.append((curr.left, dist+1))
                
            if curr.right and curr.right not in visited:
                queue.append((curr.right, dist+1))
                
            if parents[curr] and parents[curr] not in visited:
                queue.append((parents[curr], dist+1))
        
        return out