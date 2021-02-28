class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def recur(string, left, right):
            if left == n and right == n:
                self.out.append(string)
                return
            
            # only add a closing bracket if theres more opening brackets
            if left > right:
                recur(string + ')', left, right+1)
            
            if left < n:
                recur(string + '(', left+1, right)
            
        self.out = [] 
        recur('', 0, 0)
        return self.out