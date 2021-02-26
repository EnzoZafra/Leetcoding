class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        
        out = []
        for num in counter:
            if counter[num] > len(nums) / 3:
                out.append(num) 
        
        return out