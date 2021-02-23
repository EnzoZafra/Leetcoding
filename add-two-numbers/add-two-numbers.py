# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode()
        curr = dummyHead
        
        carry = 0
        
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            sum = l1val + l2val + carry
            
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(sum) 
            
            if l1:
                l1 = l1.next 
                
            if l2:
                l2 = l2.next
                
            curr = curr.next
        
        if carry:
            curr.next = ListNode(1)
    
        return dummyHead.next