class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSums = collections.defaultdict(int)
        prefixSums[0] = 1
        sumSoFar = 0
        count = 0
        
        for num in nums:
            sumSoFar += num
            diff = sumSoFar - k
            
            if diff in prefixSums:
                count += prefixSums[diff]
            
            prefixSums[sumSoFar] += 1
        
        return count