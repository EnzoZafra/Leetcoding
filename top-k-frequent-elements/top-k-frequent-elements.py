class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        heap = []
        
        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))
        
        out = []
        while k > 0:
            curr = heapq.heappop(heap)
            out.append(curr[1])
            k -= 1
        
        return out
            
            