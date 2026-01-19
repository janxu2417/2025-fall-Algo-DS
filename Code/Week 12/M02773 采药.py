t, m = map(int, input().split())
dp = [0] + [-1] * t
for i in range(m):
    ti, val = map(int, input().split())
    for j in range(t - ti, -1, -1):
        if dp[j] >= 0:
            dp[j + ti] = max(dp[j + ti], dp[j] + val)
print(max(dp))