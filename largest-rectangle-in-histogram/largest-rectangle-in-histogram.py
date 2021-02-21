class Solution(object):
    def largestRectangleAreaNLogN(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def recur(heights, start, end):

            if start > end:
                return 0

            min_index = start
            
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            
            return max(
                heights[min_index] * (end - start + 1),
                recur(heights, start, min_index-1),
                recur(heights, min_index+1, end)
            )
        
        return recur(heights, 0, len(heights)-1)
    
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0 
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            
            stack.append(i)
       
        # for the case where we reach the end and we never find heights[stack[-1]] >= heights[i]
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        
        return max_area
            