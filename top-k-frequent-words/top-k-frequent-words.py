class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)
        maxHeap = []
        out = []
        for word in counts:
            # if our maxheap is full, we need to push and pop
            heapq.heappush(maxHeap, (-1*counts[word], word))
        
        while k > 0:
            out.append(heappop(maxHeap)[1])
            k -= 1
        
        return out
                