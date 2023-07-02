class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(graph, node, been):
            if not graph[node]:
                return False
            if node in been:
                return True # cycle detected
            been.add(node)
            for n in graph[node]:
                if dfs(graph, n, been):
                    return True
            graph[node] = [] # this node leads to a dead end and not a cycle
            return False


        graph = {}
        if not prerequisites:
            return True
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        for i in range(len(prerequisites)): # building our graph
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        for i in range(numCourses): # finding a cycle in our graph means that it's impossible to attend at the both courses since they are linked to eachother | example:
            been = set()            # first A than B and at the same time first B than A
            if dfs(graph, i, been):
                return False
        return True
