class Solution(object):
    def toascii(self, num):
        
        integer = 0
        tenth_power = 0
        for i in range(len(num)-1,-1,-1):
            char = num[i]
            asciiVal = ord(char) - ord('0')
            integer += (10**tenth_power) * asciiVal
            tenth_power += 1
            
        return integer
         
        
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int1 = self.toascii(num1)
        int2 = self.toascii(num2)
        
        return str(int1*int2)
        