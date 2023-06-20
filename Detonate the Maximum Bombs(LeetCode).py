class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if math.dist(bombs[i][:2], bombs[j][:2]) <= bombs[i][2]:
                    graph[i].append(j)

        def dfs(n, visited):
            visited.add(n)
            ans = 1
        
            for neigh in graph[n]:
                if neigh not in visited:
                    ans += dfs(neigh, visited)
                    
            return ans

        ans = 0
        for i in range(len(bombs)):
            visited = set()
            ans = max(ans, dfs(i, visited))

        return ans
