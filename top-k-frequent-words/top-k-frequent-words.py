class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counts = Counter(words)
        heap = []
        for word, count in counts.items():
            heapq.heappush(heap, (-count, word))
        
        out = [] 
        while k > 0:
            out.append(heapq.heappop(heap)[1]) 
            k -= 1
        
        return out