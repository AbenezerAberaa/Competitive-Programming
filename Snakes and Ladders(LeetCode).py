class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board[0])
        
        x = 1
        y = 0
        graph = defaultdict(lambda: -1)
        for i in range(n-1, -1, -1):
            if y % 2 == 0:
                for j in range(n):
                    graph[x] = board[i][j]
                    x += 1
            else:
                for j in range(n-1, -1, -1):
                    graph[x] = board[i][j]
                    x += 1
            y += 1
        


        queue = [[1, 0]]
        visited = set()
        visited.add(1)

        if graph[(n*n)] > 0:
            return -1
        
        while (len(queue) > 0):
            x, level = queue.pop(0)
            if x == n*n:
                return level
            for i in range(x+1, x+6+1):
                if graph[i] > 0:
                    if (graph[i] not in visited):
                        visited.add(graph[i])
                        visited.add(i)
                        queue.append([graph[i], level+1])
                        
                else:
                    if (i not in visited):
                        queue.append([i, level+1])
                        visited.add(i)
        return -1
