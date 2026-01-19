x, n = map(int, input().split())
a = sorted(list(map(int, input().split())))
if a[0] != 1:
    print(-1)
else:
    tmp = 1
    ans = 1
    for i in range(1, n):
        while tmp < a[i] - 1 and tmp < x:
            tmp += a[i - 1]
            ans += 1
    if tmp < x: ans += (x - tmp + a[n - 1] - 1) // a[n - 1]
    print(ans)