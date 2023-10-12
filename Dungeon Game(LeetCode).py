class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m  = len(dungeon), len(dungeon[0])
        dp = [ [0] * m for _ in range(n)]

        def min_health_needed_for_next(cur, next_i, next_j):
            if next_i >= n or next_j >= m:
                return float('inf')
            else:
                return max(1, dp[next_i][next_j] - cur)
        
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                right = min_health_needed_for_next(dungeon[i][j], i, j+1)
                bot = min_health_needed_for_next(dungeon[i][j], i + 1, j)
                minNeedeed = min(right, bot)
                
                if minNeedeed == float('inf'):
                    dp[i][j] = 1 if dungeon[i][j] > 0 else (1 - dungeon[i][j])
                else:
                    dp[i][j] = minNeedeed
        
        return dp[0][0]
        
