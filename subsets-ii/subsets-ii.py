class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.out = []
        nums.sort()

        def backtrack(arr, start):
            self.out.append(arr[:])
            print(arr)
            
            prev = None
            for i in range(start, len(nums)):
                num = nums[i]
                
                if prev != num:
                    arr.append(num)
                    backtrack(arr, i+1)     
                    arr.pop()
                    
                prev = num
        
        backtrack([], 0)
        
        return self.out