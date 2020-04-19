"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


[
    [1, x, x],
    [x, x, x],
    [x, x, x]
]
   0, 0, 0
0, 1, 3, 1
0, 1, 5, 1
0, 4, 2, 1
#min_sum_at_x_y = min(grid[x - 1][y] + grid[x][y], grid[x][y-1] + grid[x][y] )
solution_grid[x][y] = min(solution_grid[x - 1][y], solution_grid[x][y-1]) + grid[x][y]
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        width = len(grid)
        height = len(grid[0])
        memo_grid = [[0 for x in range(height)] for y in range(width)] 
        memo_grid[0][0] = grid[0][0]

        # set up memo grid with column 1 and row 1 filled out
        for x in range(1, width):
            memo_grid[x][0] = memo_grid[x - 1][0] + grid[x][0]
            
        for y in range(1, height):
            memo_grid[0][y] = memo_grid[0][y - 1] + grid[0][y]

        # find the min sum path to the current x, y position by adding the min of either left or top position to current position
        for x in range(1, width):
            for y in range(1, height):
                memo_grid[x][y] = min(memo_grid[x - 1][y], memo_grid[x][y - 1]) + grid[x][y]

        return memo_grid[-1][-1]
