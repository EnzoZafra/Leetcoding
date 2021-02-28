class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        self.out = []
        
        def backtrack(string, start):
            if len(string) == len(S):
                self.out.append(string)
                return
            
            nextChar = S[start]
            if nextChar.isalpha():
                choices = [nextChar.lower(), nextChar.upper()]
            else:
                choices = [nextChar]
            
            for choice in choices:
                new = string+choice
                backtrack(string + choice, start+1)
                
        backtrack('', 0)
        return self.out
              
