class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ans = []
        def backtrack(string, leftParenthesisCount, rightParenthesisCount):
            if leftParenthesisCount == n and rightParenthesisCount == n:
                ans.append(string)
                return
            
            if leftParenthesisCount < n:
                backtrack(string + '(', leftParenthesisCount + 1, rightParenthesisCount)
                
            # we can only add a right parenthesis if there is already a left one.
            if rightParenthesisCount < leftParenthesisCount:
                backtrack(string + ')', leftParenthesisCount, rightParenthesisCount+1)
        
        backtrack('', 0, 0)
        return ans