class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        entrance = tuple(entrance)
        lv = 1
        seen = {entrance}
        curLv = [entrance]
        while curLv:
            nxtLv = []
            for r,c in curLv:
                for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]=="." \
                    and (nr,nc) not in seen:
                        if nr in (0,rows-1) or nc in (0,cols-1):
                            return lv
                        nxtLv.append((nr,nc))
                        seen.add((nr,nc))
            curLv = nxtLv
            lv += 1
        return -1
