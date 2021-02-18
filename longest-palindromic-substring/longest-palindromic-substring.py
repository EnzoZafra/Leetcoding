class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        longestLength = 0
        longestSubstring = ''
        for i in range(len(s)):
            for j in range(i+1):
                # if the characters are the same 
                if s[i] == s[j]:
                
                    # if its the same index, a string with two char, or if the remaining string is a palindrome too
                    if j == i or i-j == 1 or dp[i-1][j+1]:
                        dp[i][j] = True
                        if longestLength < i - j + 1:
                            longestLength = i - j + 1
                            longestSubstring = s[j:i+1]
        return longestSubstring
        
        
        