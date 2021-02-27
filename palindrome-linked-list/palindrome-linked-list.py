# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    def reverse_list(self, node):
        prev = None
        curr = node
        
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        
        return prev
    
    def restore_list(self, first_half_end, second_half_start):
        # to restore, we have to reverse the list again
        
        first_half_end.next = self.reverse_list(second_half_start)
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return True
        
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        # check if there's a palindrome
        first = head
        second = second_half_start
        
        # keep a variable for result so that the linkedlist can be restored
        while second:
            if first.val != second.val:
                # restore the list
                self.restore_list(first_half_end, second_half_start)
                return False
            
            first = first.next
            second = second.next
            
        self.restore_list(first_half_end, second_half_start)
        return True
        
