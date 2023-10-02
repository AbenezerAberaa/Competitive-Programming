class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ans = sorted(zip(ages,scores))
        dp = [i[1] for i in ans]

        for i in range(1,len(ans)):
            for j in range(i):
                if ans[i][1] >= ans[j][1]:
                    dp[i] = max(dp[i],dp[j]+ans[i][1])

        return max(dp)
