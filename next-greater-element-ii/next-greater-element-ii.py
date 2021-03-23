class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        out = [-1 for _ in range(len(nums))]
        stack = []
        
        for i in range(len(nums) * 2, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()
            
            out[i % len(nums)] = -1 if not stack else nums[stack[-1]]
            stack.append(i%len(nums))
        
        return out
            