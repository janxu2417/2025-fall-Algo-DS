def catalan(x):
    c = 1
    for i in range(1, x + 1):
        c = (4 * i - 2) * c // (i + 1)
    return c
def DP(n):
    dp = [[1 for j in range(n - i + 1)] for i in range(n)]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][1]
        for j in range(1, n - i + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j + 1]
    return dp[n - 1][1]
n = int(input())
print(catalan(n))