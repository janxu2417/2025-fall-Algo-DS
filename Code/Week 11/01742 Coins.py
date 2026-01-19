while True:
    n, m = map(int, input().split())
    if not n and not m: break
    b = list(map(int, input().split()))
    a = b[:n]
    c = b[n:]
    dp = [0] + [-1] * m
    for i in range(n):
        for j in range(m + 1):
            if dp[j] >= 0: dp[j] = c[i]
        for j in range(m - a[i] + 1):
            if dp[j] > 0:
                dp[j + a[i]] = max(dp[j + a[i]], dp[j] - 1)
    ans = 0
    for i in range(1, m + 1):
        if dp[i] >= 0: ans += 1
    print(ans)
