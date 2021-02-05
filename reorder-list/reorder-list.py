# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findMiddle(self, head):
        # find the middle 
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def reverseList(self, head):
        curr = head
        prev = None
            
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def mergeSortedLists(self, first, second):
        while second and second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp
            
        
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        middle = self.findMiddle(head)
        reversedHead = self.reverseList(middle)
        self.mergeSortedLists(head, reversedHead)

        
        
        

        