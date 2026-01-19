class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[1] * n]
        ans = (0, 0)
        for l in range(2, n + 1):
            dp.append([0] * n)
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] != s[j]: continue
                if l > 2: dp[l - 1][i] = dp[l - 3][i + 1]
                else: dp[l - 1][i] = 1
                if dp[l - 1][i]: ans = (i, j)
        return s[ans[0] : ans[1] + 1]
if __name__ == '__main__':
    s = input()
    print(Solution().longestPalindrome(s))