class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        vis = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            vis.append(temp)

        for i in range(m):
            for j in range(n):
                if (board[i][j] == 'O') and (i == 0 or i == m-1 or j == 0 or j == n-1):
                    self.dfs(board, i, j, m, n, vis)
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and vis[i][j] == 0:
                    board[i][j] = 'X'
    
    def dfs(self, board, i, j, m, n, vis):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if vis[i][j] == 1:
            return
        if board[i][j] == 'X':
            return
        vis[i][j] = 1
        self.dfs(board, i-1, j, m, n, vis)
        self.dfs(board, i+1, j, m, n, vis)
        self.dfs(board, i, j-1, m, n, vis)
        self.dfs(board, i, j+1, m, n, vis)
