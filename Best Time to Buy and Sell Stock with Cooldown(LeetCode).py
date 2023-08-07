class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp_space = [[0 for i in range(len(prices)+3)] for j in range(2)]
        for i in range(len(prices)-1, -1, -1):
            dp_space[0][i] = max(dp_space[1][i+2] + prices[i], dp_space[0][i+1])
            dp_space[1][i] = max(dp_space[0][i+1] - prices[i], dp_space[1][i+1])
        return dp_space[1][0]
