class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        min_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            min_price =min(min_price, prices[i] - max_profit)
            max_profit =max(max_profit,prices[i] - min_price - fee)

        return max_profit
