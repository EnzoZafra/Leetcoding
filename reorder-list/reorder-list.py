# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def find_middle(head):
            slow = head
            fast = head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            print(prev.val)
            return prev
        
        def merge(l1, l2):
            while l2.next:
                temp = l1.next
                l1.next = l2 
                l1 = temp
                
                temp = l2.next
                l2.next = l1
                l2 = temp
                
        if not head:
            return None
        
        middle = find_middle(head)
        l2 = reverse(middle)
        merge(head, l2)