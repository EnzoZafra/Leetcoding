"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        
        copyMap = {}
        
        curr = head
        while curr:
            currCopy = Node(curr.val)
            copyMap[curr] = currCopy
            
            curr = curr.next
        
        curr = head
        while curr:
            currCopy = copyMap[curr]
            nextCopy = copyMap.get(curr.next, None)
            randomCopy = copyMap.get(curr.random, None)
            
            currCopy.next = nextCopy
            currCopy.random = randomCopy
            
            curr = curr.next
        
        return copyMap[head]
        