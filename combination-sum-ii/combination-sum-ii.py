class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def backtrack(subset, index, sumSoFar):
            if target == sumSoFar:
                result.append(subset[:])
            elif sumSoFar > target:
                return
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    
                    subset.append(candidates[i])
                    backtrack(subset, i+1, sumSoFar + candidates[i])
                    subset.pop()
        
        result = []
        candidates.sort()
        backtrack([], 0, 0)
        
        return result
        