class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > n / 2:
                return num
        
        return -1
                
        
        