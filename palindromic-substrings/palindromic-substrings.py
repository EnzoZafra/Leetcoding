class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        
        if n == 0:
            return 0
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # base case, single subtrings
        for i in range(n):
            dp[i][i] = True
            count += 1
            
        # base case, double letter substrings 
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1  
        
        # all other cases: len of 3 to n
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
        
        return count
            