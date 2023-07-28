class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n = len(s)
        graph = defaultdict(list)
        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)
                
        visited=set()
        
        ans = [None]*n
        
        def dfs(i):
            nonlocal idxes
            visited.add(i)
            idxes.append(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)
                    
        for i in range(n):
            if i not in visited:
                idxes=[]
                dfs(i)
                st=sorted(s[i] for i in idxes)                
                for k, c in zip(sorted(idxes), st):
                    ans[k]=c
                    
                    
        return ''.join(ans)
