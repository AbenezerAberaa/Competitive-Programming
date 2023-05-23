from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def bfs(i,j):
            #Mark this as visited
            grid2[i][j] = 0
            q = deque([(i,j)])
            flag = True
            while q:
                x,y = q.popleft()
                if grid1[x][y] == 0:
                    flag = False
                for xd,yd in dirs:
                    new_x = x+xd
                    new_y = y+yd
                    if 0 <= new_x < m and 0 <= new_y < n and grid2[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        grid2[new_x][new_y] = 0
            return flag

        m = len(grid2)
        n = len(grid2[0])
        count = 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid2[i][j] == grid1[i][j]:
                    if bfs(i,j):
                        c
