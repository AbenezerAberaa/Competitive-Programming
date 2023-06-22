class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        d = deque()
        if grid[0][0] != 0:
            return -1
        d.append((0, 0))
        ans = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        shift_x = [1, 0, -1, 0, 1, 1, -1, -1]
        shift_y = [0, 1, 0, -1, -1, 1, 1, -1]
        ans[0][0] = 1

        def is_valid(new_x, new_y):
            return 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])

        while d:
            prev_x, prev_y = d.popleft()
            
            for dx, dy in zip(shift_x, shift_y):
                new_x = prev_x + dx
                new_y = prev_y + dy
                if not is_valid(new_x, new_y):
                    continue
                if grid[new_x][new_y] == 0 and ans[new_x][new_y] > ans[prev_x][prev_y] + 1:
                    ans[new_x][new_y] = ans[prev_x][prev_y] + 1
                    d.append((new_x, new_y))
        return ans[-1][-1] if ans[-1][-1] != float('inf') else -1
