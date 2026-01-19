t = int(input())
maxA = 1_000_001
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[-maxA, -maxA], [-maxA, -maxA]]
    for i in range(n):
        dp[0][0] = max(dp[0][0], - a[i])
        dp[0][1] = max(dp[0][1], dp[0][0] + a[i])
        dp[1][0] = max(dp[1][0], dp[0][1] - a[i])
        dp[1][1] = max(dp[1][1], dp[1][0] + a[i])
    print(dp[1][1])