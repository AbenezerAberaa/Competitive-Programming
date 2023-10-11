class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: x[0] - x[1])
        ans = 0
        n = len(costs)
        middle = n // 2

        for i in range(middle):
            ans += costs[i][0]
        for j in range(middle, n):
            ans += costs[j][1]
        return ans
