class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        word1len = len(word1)
        word2len = len(word2)
        
        if word1len == 0:
            return word2len
        
        if word2len == 0:
            return word1len
        
        dp = [[0 for _ in range(word2len+1)] for _ in range(word1len+1)]
        
        for row in range(word1len+1):
            dp[row][0] = row
        
        for col in range(word2len+1):
            dp[0][col] = col
        
        for row in range(1, word1len+1):
            for col in range(1, word2len+1):
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                
                else:
                    removeFromWord1 = dp[row-1][col]
                    addToWord1 = dp[row][col-1]
                    replaceAChar = dp[row-1][col-1]
                    
                    dp[row][col] = min(removeFromWord1, addToWord1, replaceAChar) + 1
       
        return dp[-1][-1]