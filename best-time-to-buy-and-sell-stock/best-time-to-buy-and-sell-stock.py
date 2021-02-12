class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        # store the max price up to i
        max_right_scan = [-1 for _ in range(len(prices))]
        
        max_right_scan[-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            price = prices[i]
            max_right_scan[i] = max(price, max_right_scan[i+1])
        
        print(max_right_scan)
        
        maxProfit = 0
        minBuyPrice = float('inf')
        for i in range(len(prices)):
            price = prices[i]
            minBuyPrice = min(minBuyPrice, price)
            maxProfit = max(maxProfit, max_right_scan[i] - minBuyPrice)
        
        return maxProfit
        