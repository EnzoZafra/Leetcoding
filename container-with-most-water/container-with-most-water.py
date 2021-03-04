class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        maxArea = float('-inf')
        while start < end:
            width = end - start
            curr_height = min(height[start], height[end])
            maxArea = max(maxArea, width * curr_height)
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return maxArea
            