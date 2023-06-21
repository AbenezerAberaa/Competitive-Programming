class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
  
        color = [-1] * (n + 1)
        q = deque()
        for i, c in enumerate(color):
            
            if c != -1: continue
            
            q.append(i) 
            c = 'R'
            
            while q:
                node = q.popleft()
                
                for child in graph[node]:
                    print(child)
                    if color[child] == -1:
                        if color[node] == 'R':
                            color[child] = 'B'
                            
                        else:
                            color[child] = 'R'
                            
                        q.append(child)
                        
                        
                    elif color[child] == color[node]:
                        return False
                
        return True
