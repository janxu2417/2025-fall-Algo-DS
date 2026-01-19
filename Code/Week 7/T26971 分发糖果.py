n = int(input())
rt = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    if rt[i] > rt[i - 1]: dp[i] = max(dp[i], dp[i - 1] + 1)
for i in range(n - 2, -1, -1):
    if rt[i] > rt[i + 1]: dp[i] = max(dp[i], dp[i + 1] + 1)
print(sum(dp))