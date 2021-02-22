class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        out = [0 for _ in range(len(T))]
        
        stack = []
        for i in range(len(T)-1,-1,-1):
            # get rid of the temperatures in the stack that are colder
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            
            if stack:
                out[i] = stack[-1] - i
            
            stack.append(i)
        
        return out
                