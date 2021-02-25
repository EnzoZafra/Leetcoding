class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        minIndexSum = float('inf')
        indexSums = collections.defaultdict(list)
        
        indexList1 = {}
        indexList2 = {}
        
        for index, restaurant in enumerate(list1):
            indexList1[restaurant] = index
            
        for index, restaurant in enumerate(list2):
            indexList2[restaurant] = index
        
        
        for restaurant in indexList2:
            if restaurant in indexList1:
                indexSum = indexList2[restaurant] + indexList1[restaurant]
                indexSums[indexSum].append(restaurant)
                minIndexSum = min(minIndexSum, indexSum)
        
        return indexSums[minIndexSum]
            
        
            
        
        