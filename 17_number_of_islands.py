class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        width = len(grid) 
        height = len(grid[0]) 
        num_islands = 0
        for x in range(width):
            for y in range(height):
                if grid[x][y] == '1': # we've found some land
                    num_islands += 1
                    Solution.dfs(grid, width, height, x, y) # flood fill
        return num_islands
    
    def dfs(grid, width, height, x, y):
        if x >= 0 and x <= width - 1  and y >= 0 and y <=  height - 1:
            if grid[x][y] == '0':
                return
            else:
                grid[x][y] = '0'

            Solution.dfs(grid, width, height, x, y + 1)
            Solution.dfs(grid, width, height, x, y - 1)
            Solution.dfs(grid, width, height, x + 1, y)
            Solution.dfs(grid, width, height, x - 1, y)
