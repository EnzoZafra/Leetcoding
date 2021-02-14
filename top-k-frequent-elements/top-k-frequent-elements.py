class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        
        maxHeap = []
        
        for num in counter:
            heapq.heappush(maxHeap, (-counter[num], num))
        
        out = []
        while k > 0:
            out.append(heapq.heappop(maxHeap)[1])
            k -= 1
        
        return out