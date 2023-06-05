class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        maxu = 0
        def dfs(i,j):
            if 0 <= i < row and 0 <= j < col and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j)
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    maxu = max(dfs(i,j), maxu)
        return maxu
