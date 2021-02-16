class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def backtrack(arr, start, target_left):
            if target_left == 0:
                ans.append(arr[:])
                return
            
            if target < 0:
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                num = candidates[i]
                
                if target_left - num < 0:
                    break
                    
                arr.append(num)
                backtrack(arr, i+1, target_left-num)
                arr.pop()
                 
        
        candidates.sort()
        ans = []
        backtrack([], 0, target)
        return ans
                
                