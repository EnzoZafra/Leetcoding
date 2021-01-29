# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        numLists = len(lists)
        interval = 1
        
        while interval < numLists:
            for i in range(0, numLists - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            
            interval *= 2
            
        return lists[0]
    
    def merge2Lists(self, l1, l2):
        head = ListNode()
        curr = head
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return head.next