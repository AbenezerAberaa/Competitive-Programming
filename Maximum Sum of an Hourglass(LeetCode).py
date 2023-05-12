class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def hourglassSum(i, j):
            return sum(grid[i - 1][j - 1:j + 2]) + grid[i][j] + sum(grid[i + 1][j - 1:j + 2])
        
        maxu = 0
        for i, j in product(range(1, row - 1), range(1, col - 1)):
            maxu = max(maxu, hourglassSum(i, j))
            
        return maxu
