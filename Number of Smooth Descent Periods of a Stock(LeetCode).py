class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        ans = 1  # prices[0]
        dailyPrice = 1

        for index in range(1, len(prices)):
            if prices[index] == prices[index - 1] - 1:
                dailyPrice += 1
            else:
                dailyPrice = 1
            ans += dailyPrice

        return ans
