class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.traverse(res, 0, graph, [])
        return res 
    
    def traverse(self, res, i, graph, path):
        path.append(i)

        n = len(graph)
        if i == n - 1:
            res.append(list(path))
        
        for neighbor in graph[i]:
            self.traverse(res, neighbor, graph,path)

        del path[-1]
