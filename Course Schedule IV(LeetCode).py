class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def my_bfs_fun(root, dest):
            
            stack = deque([root])
            seen = set()
            
            while stack:
                
                item = stack.popleft()
                if item == dest:
                    return True
                for child in graph[item]:
                    
                    if child not in seen:
                        seen.add(child)
                        stack.append(child)
            return False
        
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
         
        res = []
        for a, b in queries:
            
            res.append(my_bfs_fun(a, b))
        return res
