class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        constraint = length / 3
        counter = collections.defaultdict(int)
        out = set()
        
        for num in nums:
            counter[num] += 1
            if counter[num] > constraint:
                out.add(num)
        
        return out