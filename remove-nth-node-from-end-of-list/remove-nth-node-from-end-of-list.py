# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        while n > 0:
            fast = fast.next
            n -= 1
        
        if not fast:
            return head.next
        
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next
            
        
        return head
        