class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        longestLength = 0
        longestSubstring = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                # if the characters are the same 
                if s[i] == s[j]:
                
                    # if its a string with two char, or if the remaining string is a palindrome too
                    if j == i or j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if longestLength < j - i + 1:
                            longestLength = j - i + 1
                            longestSubstring = s[i:j+1]
                            
        return longestSubstring
        
        
        