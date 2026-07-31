class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for k in range(n - 1, -1, -1):        # text2 index
            for j in range(m - 1, -1, -1):    # text1 index
                if text1[j] == text2[k]:
                    dp[k][j] = 1 + dp[k + 1][j + 1]
                else:
                    dp[k][j] = max(dp[k + 1][j], dp[k][j + 1])

        return dp[0][0]