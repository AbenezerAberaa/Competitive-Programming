class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        if not matrix:
            return False
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//cols][mid%cols] == target:
                return True
            elif matrix[mid//cols][mid%cols] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return False
