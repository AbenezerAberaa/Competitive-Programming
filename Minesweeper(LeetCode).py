class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cols = len(board[0])
        rows = len(board)
        seen = set()
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        memo = set()
        q = [click]
        while q:
            i, j = q.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            num = 0
            tem = []
            for s in steps:
                i1, j1 = i + s[0], j + s[1]
                if i1 >= 0 and i1 < rows and j1 >= 0 and j1 < cols:
                    if board[i1][j1] == 'M':
                        num += 1
                    elif board[i1][j1] == 'E':
                        tem.append((i1, j1))
            if num:
                board[i][j] = str(num)
            else:
                board[i][j] = 'B'
                q += tem
        return board
