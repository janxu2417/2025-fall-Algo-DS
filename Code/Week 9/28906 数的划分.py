n, m = map(int, input().split())
dp = [[0]]
for i in range(1, n + 1):
    dp.append([0 for j in range(i + 1)])
    dp[i][i] += 1

for k in range(2, m + 1):
    for i in range(n, k - 1, -1):
        dp[i][0] = 0
        for j in range(1, i - k + 2):
            dp[i][j] = dp[i][j - 1] + dp[i - j][min(j, i - j - k + 2)]
            #for t in range(max(1, (i - j) // k), min(j + 1, i - j - k + 3)):
            #    dp[i][j][k % 2] += dp[i - j][t][(k + 1) % 2]

print(dp[n][n - m + 1])