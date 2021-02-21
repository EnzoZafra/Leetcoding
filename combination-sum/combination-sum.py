class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        self.out = []
        
        def backtrack(arr, sumSoFar, start):
            if sumSoFar == target:
                self.out.append(arr[:])
            elif sumSoFar > target:
                return
            else:
                for i in range(start, len(candidates)):
                    num = candidates[i] 
                    arr.append(num)
                    backtrack(arr, sumSoFar + num, i)
                    arr.pop()
        
        backtrack([], 0, 0)
        return self.out
                