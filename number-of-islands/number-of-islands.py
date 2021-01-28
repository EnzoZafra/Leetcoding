class Solution(object):
    
    def dfs(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = 'visited'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    
    def dfs_iter(self, grid, i, j):
        rowCol = [-1, 0, 0, 1]
        colCol = [0, -1, 1, 0]
        stack = []
        
        stack.append((i,j))
        
        while stack:
            curr = stack.pop()
            grid[curr[0]][curr[1]] = 'visited'
            
            for i in range(4):
                x = curr[0] + rowCol[i]
                y = curr[1] + colCol[i]
                
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '1':
                    stack.append((x, y))
                    print((x,y))
            
        
        
            
            
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1;
                    self.dfs_iter(grid, i, j)
        
        return ans
                    