class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        for row in range(0, len(grid) - 2):
            maxu = []
            for col in range(0, len(grid[0]) - 2):
                v1 = max(grid[row][col], grid[row][col + 1], grid[row][col + 2])
                v2 = max(grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2])
                v3 = max(grid[row + 2][col], grid[row + 2][col + 1], grid[row + 2][col + 2])
                maxu.append(max(v1, v2, v3))
            
            res.append(maxu)
        
        return res
