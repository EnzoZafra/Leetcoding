# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        start = head
        prev = None
        
        while m > 1:
            prev = start
            start = start.next
            m -= 1
            n -= 1
            
        tail = start
        con = prev
        
        while n:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
            n -= 1
        
        if con:
            con.next = prev
        else:
            head = prev
        
        tail.next = start
        
        return head
    