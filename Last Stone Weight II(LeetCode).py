class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        max_weight = int(total/2)

        dp = [0]*(max_weight+1)

        for stone in stones:
            for weight in range(max_weight,-1,-1):
                if weight - stone >= 0:
                    dp[weight] = max(dp[weight], stone + dp[weight-stone])
        ans = total - 2*dp[-1]
        return ans
        
