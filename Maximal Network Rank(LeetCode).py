class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for a,b in roads:
            dic[a].append(b)
            dic[b].append(a)
        maxu = 0
        for i in range(n):
            for j in range(i+1,n):
                x=len(dic[i])+len(dic[j])
                if j in dic[i]:
                    x-=1
                maxu = max(maxu, x)
        return maxu
