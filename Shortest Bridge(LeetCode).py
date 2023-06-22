class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def find_islands(r,c):
            if r < 0 or r >= n or c < 0 or c >= n or (r,c) in visited or grid[r][c] == 0: return 
            visited.add((r,c))
            queue.append([r,c])
            
            find_islands(r+1,c)
            find_islands(r-1,c)
            find_islands(r,c+1)
            find_islands(r,c-1)

        found = False
        for i in range(n):
            if found: break
            for j in range(n):
                if grid[i][j] == 0: continue
                find_islands(i,j)
                
                if len(queue) > 0:
                    found = True
                    break
        found = False
        res = 0
        while len(queue) > 0:
            temp = []
            for r,c in queue:
                for i,j in directions:
                    if 0 <= r+i < n and 0 <=c+j < n and (r+i,c+j) not in visited and grid[r+i][c+j] == 1:
                        found = True
                        break
                    if 0 <= r+i < n and 0 <=c+j < n and (r+i,c+j) not in visited:
                        temp.append([r+i,c+j])
                        visited.add((r+i,c+j))
                if found: break
                queue = temp
            if found: break
            res += 1
            
            
        return res 
