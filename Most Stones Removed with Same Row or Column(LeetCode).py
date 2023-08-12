class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def dfs(rows, cols, r, c, visited):
            visited.add((r,c))
            for row,col in rows[r]:
                if (row,col) not in visited:
                    dfs(rows, cols, row, col, visited)
            for row,col in cols[c]:
                if (row,col) not in visited:
                    dfs(rows, cols, row, col, visited)
                    
        rows, cols = {}, {}
        
        for r,c in stones:

            rows[r] = rows.get(r,[])+[(r,c)]
            cols[c] = cols.get(c,[])+[(r,c)]

        shared = 0
        visited = set()

        for r, c in stones:
            if (r,c) not in visited:
                shared += 1
                dfs(rows, cols, r, c, visited)

        return len(stones) - shared
