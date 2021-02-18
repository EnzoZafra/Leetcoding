class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        heap = []
        out = []
        
        for restaurant in restaurants:
            if veganFriendly and not restaurant[2]:
                continue
            
            if restaurant[4] > maxDistance:
                continue
            
            if restaurant[3] > maxPrice:
                continue
            
            heap.append((restaurant[0], restaurant[1]))
        
        heap = sorted(heap, key=lambda x: (x[1], x[0]), reverse=True)
        
        return [x[0] for x in heap]
        