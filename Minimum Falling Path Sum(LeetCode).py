class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        prev = [matrix[0][j] for j in range(cols)]
        for i in range(1, rows):
            row = [0] * cols
            for j in range(cols):
                row[j] = prev[j] + matrix[i][j]
                if j > 0:
                    row[j] = min(row[j], prev[j-1] + matrix[i][j])
                if j < cols-1:
                    row[j] = min(row[j], prev[j+1] + matrix[i][j])
            prev = row
        return min(prev)
