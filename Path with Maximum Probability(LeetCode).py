class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        g = {}
        for i in range(n):
            g[i] = []

        for i in range(len(edges)):
            u, v = edges[i]
            g[u].append((v, succProb[i]))
            g[v].append((u, succProb[i]))

        
        d = {v: 0 for v in g}
        d[start_node] = 1
        q = [(-1, start_node)]

        while q:
            cur_dist, cur_v = heapq.heappop(q)
            cur_dist *= -1
            if cur_dist < d[cur_v]:
                continue

            for nb, w in g[cur_v]:
                new_dist = cur_dist * w
                if new_dist > d[nb]:
                    d[nb] = new_dist
                    heapq.heappush(q, (-new_dist, nb))

        return d[end_node]
        
