# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def print_ll(self, head):
        temp = head
        seen = set()
        while temp:
            if temp in seen:
                print('cycle')
                return
            else:
                print(temp.val)
                seen.add(temp)
                temp = temp.next
                
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = []
        
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        
        curr = head
        
        while curr:
            temp = curr.next
            end = stack.pop()
            
            curr.next = end
            curr = temp
            end.next = curr
            
            if curr and curr.next == end:
                curr.next = None  
                break
        
        return head