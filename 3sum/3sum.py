class Solution(object):
    def twoSum(self, nums, res, i):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
                    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        # fix A, then two sum for B and C
        out = []
        for i, a in enumerate(nums):
            # a must be negative
            if a > 0:
                continue
            
            # if a different number
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, out, i) 
                    
        return out
            
            