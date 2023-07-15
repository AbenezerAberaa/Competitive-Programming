class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dyna_pro = [-1] * len(graph)
        def dfs(node):
            if dyna_pro[node] != -1:
                return dyna_pro[node]
            if len(graph[node]) == 0:
                dyna_pro[node] = True
                return True
            dyna_pro[node] = False
            is_safe_node = True
            for next_node in graph[node]:
                is_safe_node = is_safe_node and dfs(next_node)
            dyna_pro[node] = is_safe_node
            return dyna_pro[node]
        ans = []
        for i in range(len(graph)):
            dfs(i)
            if dyna_pro[i]:
                ans.append(i)
        return ans
