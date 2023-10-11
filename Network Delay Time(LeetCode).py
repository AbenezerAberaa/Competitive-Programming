class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        adj = [[] for _ in range(n+1)]

        for i in range(len(times)):
            u = times[i][0]
            v = times[i][1]
            w = times[i][2]

            adj[u].append([v,w])


        distance = [1e9]*(n+1)
        distance[k] = 0

        q = [[0, k]]

        while q:
            node = q.pop(0)
            signal = node[0]
            vertex = node[1]

            for i in adj[vertex]:
                v = i[0]
                w = i[1]

                if w  + signal < distance[v]:
                    distance[v] = signal + w
                    q.append([signal + w , v])

        distance.pop(0)
        ans = max(distance)
        if ans == 1e9:
            return -1

        return ans
        
