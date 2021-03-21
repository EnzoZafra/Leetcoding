"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        copies = {}
        copies[head] = Node(head.val)
        
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = copies[curr]
            randomCopy = copies[curr.random] if curr.random else None
            nextCopy = copies[curr.next] if curr.next else None
            
            copy.random = randomCopy
            copy.next = nextCopy
            
            curr = curr.next
        
        return copies[head]