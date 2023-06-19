class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph_dict = defaultdict(list)

        for i in range(len(edges)):
            source: int = edges[i][0]
            dest: int = edges[i][1]
            graph_dict[source].append(dest)
            graph_dict[dest].append(source)

        ans_list = [0]*n

        def dfs(source, parent):
            alpha_list = [0]*26
            alpha_list[ord(labels[source])-97]+=1
            for node in graph_dict[source]:
                if node == parent:
                    continue
                temp = dfs(node,source)
                for i in range(len(temp)):
                    alpha_list[i]+=temp[i]
            ans_list[source]=alpha_list[ord(labels[source])-97]

            return alpha_list

        dfs(0,-1)
        return ans_list
