class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(1, n + 1):
            k = i % 2
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[k][j] = dp[k ^ 1][j - 1] + 1
                else:
                    dp[k][j] = max(dp[k][j - 1], dp[k ^ 1][j])
        return max(dp[n % 2])
if __name__ == '__main__':
    sol = Solution()
    while True:
        try:
            s1, s2 = input().split()
            print(sol.longestCommonSubsequence(s1, s2))
        except EOFError:
            break