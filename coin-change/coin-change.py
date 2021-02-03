class Solution(object):
    def coinChange2D(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        R = amount
        C = len(coins)
        
        dp = [[float('inf') for _ in range(C)] for x in range(R+1)]
        
        for i in range(C):
            dp[0][i] = 0
        
        for coinIndex in range(C):
            coin = coins[coinIndex-1]
            for amountIndex in range(coin, R+1):
                
                from_above = dp[amountIndex][coinIndex - 1]
                from_left = dp[amountIndex-coin][coinIndex]
                dp[amountIndex][coinIndex] = min(from_left + 1, from_above)
        
        return dp[R][C-1]
    
    def coinChange(self, coins, amount):
        
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                # either we take the count of the previous coin that can make up X amount
                # or we take the current coin and the count of the difference in amount
                dp[x] = min(dp[x], dp[x-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
            
        
        
