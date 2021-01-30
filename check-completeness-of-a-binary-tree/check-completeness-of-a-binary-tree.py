# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque()
        q.append(root)
        ended = False

        # do BFS and check if we pop a null node before the end
        while q:
            curr = q.popleft()

            # we popped an empty
            if not curr:
                ended = True

            else:
                if ended:
                    return False
                
                q.append(curr.left)
                q.append(curr.right)
        
        return True