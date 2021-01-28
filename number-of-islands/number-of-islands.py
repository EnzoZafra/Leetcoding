class Solution(object):
    
    
    def dfs_iter(self, grid, i, j):
        rows = [-1, 0, 0, 1]
        cols = [0, -1, 1, 0]
        stack = []
        
        stack.append((i,j))
        
        # do DFS and mark as visited 
        while stack:
            curr = stack.pop()
            grid[curr[0]][curr[1]] = '0'
            
            for index in range(len(rows)):
                y = curr[0] + rows[index]
                x = curr[1] + cols[index]
                
                # check that its not out of bounds and is land
                if x >= 0 and y>=0 and x<len(grid[0]) and y<len(grid) and grid[y][x] == '1':
                    stack.append((y, x))
            
            
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # found a new island
                if grid[i][j] == '1':
                    ans += 1;
                    # DFS and mark all "lands" of that island
                    self.dfs_iter(grid, i, j)
        
        return ans
                    