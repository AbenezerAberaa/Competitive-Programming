class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp_arr = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                dp_arr[j] += dp_arr[j - 1]

        return dp_arr[n - 1]
