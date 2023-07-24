class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        parent = [i for i in range(n)]
        
        def union_find(x):
            if parent[x]!=x:
                parent[x] = union_find(parent[x])
            return parent[x]

        def Its_union(x,y):
            parent[union_find(x)] = union_find(y)

        
        for u,v in edges:
            Its_union(u,v)

        return (union_find(source) == union_find(destination))
