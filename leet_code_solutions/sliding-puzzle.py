class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        board = board[0] + board[1]
        
        ans = 0 
        seen = set([tuple(board)])
        queue = [board]
        while queue: 
            newq = []
            for x in queue: 
                if x == [1,2,3,4,5,0]: return ans 
                k = x.index(0)
                for kk in (k-1, k+1, k-3, k+3): 
                    if 0 <= kk < 6 and (k, kk) not in ((2, 3), (3, 2)):
                        xx = x.copy()
                        xx[k], xx[kk] = xx[kk], xx[k]
                        if tuple(xx) not in seen: 
                            seen.add(tuple(xx))
                            newq.append(xx)
            queue = newq 
            ans += 1
        return -1 
        