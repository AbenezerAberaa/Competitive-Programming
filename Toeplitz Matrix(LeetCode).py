class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        i, j = rows - 1, 0
        while i != 0 or j != cols - 1:
            y, z = i, j
            res = matrix[y][z]
            while z >= 0 and y >= 0:
                if matrix[y][z] != res:
                    return False
                z -= 1; y -= 1
            if j < cols-1:
                j += 1
            else:
                i -= 1
        return True
