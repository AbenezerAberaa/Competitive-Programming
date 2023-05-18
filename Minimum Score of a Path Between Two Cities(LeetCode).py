class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = {i : float("inf") for i in range(1,n+1)}
        print(ans)
        parent = {i:i for i in range(1,n+1)}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y,dist):
            xrep = find(x)
            yrep = find(y)
            
            parent[yrep] = xrep
            ans[xrep] = min(ans[xrep],ans[yrep],dist)

        for a,b,c in roads:
            union(a,b,c)
            
        return ans[find(1)]
