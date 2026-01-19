n, a, b, c = map(int, input().split())
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in [i - a, i - b, i - c]:
        if j >= 0 and dp[j] >= 0:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp[n])