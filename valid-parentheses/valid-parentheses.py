class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        stack = []
        
        for char in s:
            # if opening bracket, append to stack
            if char in brackets.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                # pop the stack
                currBracket = stack.pop()
                if currBracket != brackets.get(char):
                    return False
        
        return len(stack) == 0