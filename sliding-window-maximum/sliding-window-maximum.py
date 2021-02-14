class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n * k == 0:
            return []
        
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove indexes of elements that are not in the sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
            
            # remove from deq indexes of all elements
            # that are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
                
        output = [nums[max_idx]]
        
        for i in range(k,n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        
        return output
        
        
    def maxSlidingWindowTle(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n * k == 0:
            return []
        
        if k == 1:
            return nums
        
        start = 0
        end = 0
        
        out = []
        
        currMax = float('-inf')
        while end < k:
            currMax = max(currMax, nums[end]) 
            end += 1
        
        out.append(currMax)
        
        while end < len(nums):
            new_num = nums[end]
            removed_num = nums[start]
            
            start += 1
            end += 1
            
            if removed_num == currMax:
                currMax = max(nums[start:end])
            else:
                currMax = max(currMax, new_num)
            
            out.append(currMax)
            
        return out