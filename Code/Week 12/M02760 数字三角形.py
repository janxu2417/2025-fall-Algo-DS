n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in range(i, 0, -1):
        dp[j] = max(dp[j], dp[j - 1]) + a[j - 1]
print(max(dp))