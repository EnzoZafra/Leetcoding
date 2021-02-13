# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next)
        l1Ptr = l1
        l2Ptr = l2
        
        curr = dummy 
        while l1Ptr and l2Ptr:
            if l1Ptr.val < l2Ptr.val:
                curr.next = l1Ptr
                l1Ptr = l1Ptr.next
            else:
                curr.next = l2Ptr
                l2Ptr = l2Ptr.next
            
            curr = curr.next
        
        if l1Ptr:
            curr.next = l1Ptr
        
        if l2Ptr:
            curr.next = l2Ptr
        
        return dummy.next
        