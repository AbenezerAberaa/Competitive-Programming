class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        dict_ = defaultdict(list)
        for u,v in edges:
            dict_[u].append(v)
            dict_[v].append(u)
        
        nuclear = {}
        height = {}
        def mark_par(x,p,h):
            nuclear[x] = p
            height[x] = h
            for c in dict_[x]:
                if c == p: continue
                mark_par(c, x, h+1)
        mark_par(0, -1, 0)
    
        cnt = defaultdict(int)
        for s,e in trips:
            if height[s] < height[e]:
                s,e = e,s
            while height[s] > height[e]: 
                cnt[s] += 1
                s = nuclear[s]
            while e!=s:
                cnt[s] += 1
                cnt[e] += 1
                s = nuclear[s]
                e = nuclear[e]
            cnt[s] += 1
     
        @cache
        def f(x):
            return min((price[x]//2*cnt[x] + sum(g(c) for c in dict_[x] if c != nuclear[x])), g(x))
        @cache
        def g(x):
            return price[x]*cnt[x] + sum(f(c) for c in dict_[x] if c != nuclear[x])
        return f(0)
        
