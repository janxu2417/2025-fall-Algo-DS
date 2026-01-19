n = int(input())
a = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]
ans = 1
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]: dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        if a[j] > a[i]: dp[i][0] = max(dp[i][0], dp[j][1] + 1)
    ans = max(ans, max(dp[i][0], dp[i][1]))
print(ans)