class Solution(object):
    def editDistance(self, word1, word2, m, n):
        # if word1 is an empty string, return the length of word2 because we need to insert that many
        if m == 0:
            return n
        # if word2 is an empty string, return the length of word 1 beause we need to remove that many 
        if n == 0:
            return m
        
        # if the last characters of each are the same, recur
        if word1[m-1] == word2[n-1]:
            return self.editDistance(word1, word2, m-1, n-1)
        else:
            insert = self.editDistance(word1, word2, m, n-1) # inserting into word1 is like removing a char from word2
            remove = self.editDistance(word1, word2, m-1, n) # removing a char from word1
            replace = self.editDistance(word1, word2, m-1, n-1) # replacing 
            return 1 + min(insert, remove, replace)
            
        
        
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        R = len(word1) + 1
        C = len(word2) + 1
        
        dp = [[0 for _ in range(C)] for _ in range(R)]
        
        # fill base case
        for i in range(R):
            dp[i][0] = i
        
        for i in range(C):
            dp[0][i] = i
            
        for row in range(1,R):
            for col in range(1,C):
                # check if the characters are the same
                if word1[row-1] == word2[col-1]:
                    # then its just the same distance as the last subproblem (diagonally)
                    dp[row][col] = dp[row-1][col-1]
                else:
                    add_char = dp[row][col-1]
                    remove_char = dp[row-1][col]
                    replace_char = dp[row-1][col-1]
                    dp[row][col] = 1 + min(add_char, remove_char, replace_char)
        print(dp)
        return dp[R-1][C-1]
                    
        