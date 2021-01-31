class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(subset, currIndex):
            # append subset to our output
            # since python lists are passed by reference, we need to append a copy
            superset.append(subset[:])

            # 1. Choose from a list of options and add it to our subset
            for i in range(currIndex, len(nums)):
                subset.append(nums[i])

                # 2. This question does not have constraints

                # 3. Recurse
                backtrack(subset, i+1)

                # 4. Remove the choice from step 1
                subset.pop()
        
        superset = []
        backtrack([], 0)
        nums.sort()
        
        return superset