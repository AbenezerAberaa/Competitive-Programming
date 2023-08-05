class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp_arr = [float('inf')] * (amount + 1)
        dp_arr[0] = 0
        for coin in coins:
            for j in range(coin, amount +1):
                dp_arr[j] = min(dp_arr[j], dp_arr[j-coin]+1)
        return dp_arr[amount] if dp_arr[amount] != float('inf') else -1
