class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1 = len(text1)
        len2 = len(text2)
        
        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
        
        for col in range(1, len1+1):
            for row in range(1, len2+1):
                if text1[col-1] == text2[row-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]