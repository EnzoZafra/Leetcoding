class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPriceRight = [0 for x in range(len(prices))]
        maxPriceRight[-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxPriceRight[i] = max(maxPriceRight[i+1], prices[i])
        
        maxProfit = 0
        minPriceSoFar = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            minPriceSoFar = min(minPriceSoFar, price)
            maxProfit = max(maxProfit, maxPriceRight[i] - minPriceSoFar)
        
        return maxProfit
            