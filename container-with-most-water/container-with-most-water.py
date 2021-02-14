class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # two pointer, one at the start and one at the end
        # height = min(height[start], height[end])
        # width = end - start + 1
        # keep the ptr with the longer bar
        
        start = 0
        end = len(height) - 1
        maxArea = 0 
        while start < end:
            height1 = height[start]
            height2 = height[end]
            maxHeight = min(height1, height2)
            width = end - start
            maxArea = max(maxArea, maxHeight * width)
            
            if height1 > height2:
                end -= 1
            else:
                start += 1
                
        return maxArea