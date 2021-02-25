class Solution(object):
    def countBit(self, num):
        count = 0
        while num > 0:
            count += num & 1
            num = num >> 1
        
        return count
        
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        out = []
        for i in range(num+1):
            out.append(self.countBit(i))
        
        return out
        