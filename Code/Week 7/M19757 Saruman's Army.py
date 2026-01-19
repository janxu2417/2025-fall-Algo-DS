while True:
    r, n = map(int, input().split())
    if r < 0: break
    a = sorted(list(map(int, input().split())))
    ans, lf, j = 0, 0, 1
    mid = 0
    while j < n:
        while j < n and a[j] - a[lf] <= r * 2:
            while a[j] - a[mid] > r : mid += 1
            if a[mid] - a[lf] <= r: j += 1
            else: break
        ans += 1
        lf, mid, j = j, j, j + 1
    if lf < n: ans += 1
    print(ans)