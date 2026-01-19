mod = 1000000007
t, k = map(int, input().split())
dp = [0] * (10 ** 5 + 1)
dp[0] = 1
for i in range(1, 10 ** 5 + 1):
    dp[i] = dp[i - 1]
    if i >= k: dp[i] += dp[i - k]
    dp[i] %= mod
for i in range(1, 10 ** 5 + 1):
    dp[i] = (dp[i] + dp[i - 1]) % mod
for i in range(t):
    a, b = map(int, input().split())
    print((dp[b] - dp[a - 1] + mod) % mod)