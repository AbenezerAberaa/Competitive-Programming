class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        dp_dic = [[0] * n for i in range(n)]

        for i in range(n - 1, -1, -1):
            dp_dic[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp_dic[i][j] = dp_dic[i + 1][j - 1] + 2
                else:
                    dp_dic[i][j] = max(dp_dic[i + 1][j], dp_dic[i][j - 1])

        return dp_dic[0][n - 1]
