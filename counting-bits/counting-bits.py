class Solution:
    def countOnes(self, num):
        count = 0
        while num > 0:
            if num & 1:
                count += 1
            
            num = num >> 1
        
        return count
        
    def countBits(self, num: int) -> List[int]:
        out = []
        
        for i in range(num+1):
            out.append(self.countOnes(i)) 
        
        return out