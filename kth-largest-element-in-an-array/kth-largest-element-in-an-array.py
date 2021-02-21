class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -num)
        
        while k > 1:
            heapq.heappop(heap) 
            k -= 1
        
        return -1 * heapq.heappop(heap)