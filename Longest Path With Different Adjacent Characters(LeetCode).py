class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        size = len(parent)
        if size == 1:
            return 1

        result = 0
        familySize = [0] * size
        for each in range(1, size):
            familySize[parent[each]] += 1
        longest = [ 0 for _ in parent]
        nexts = [ 0 for _ in parent]

        arr = []
        for i in range(1,size):
            if familySize[i] == 0:
                arr.append(i)

        while arr:
            node = arr.pop()
            par = parent[node]
            familySize[par] -= 1
            if s[node] != s[par]:
                if longest[par] < longest[node]+1:
                    nexts[par] = longest[par]
                    longest[par] = longest[node]+1
                elif nexts[par] < longest[node]+1:
                    nexts[par] = longest[node]+1
            if familySize[par] == 0:
                arr.append(par)
                result = max(result, longest[par] + nexts[par]+1)

        return result
        
