n, b = map(int, input().split())
val = list(map(int, input().split()))
w = list(map(int, input().split()))
dp = [0] + [-1] * b
for i in range(n):
    for j in range(b - w[i], -1, -1):
        if dp[j] != -1:
            dp[j + w[i]] = max(dp[j + w[i]], dp[j] + val[i])
print(max(dp))