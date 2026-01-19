t = int(input())
for _ in range(t):
    L, n = map(int, input().split())
    v = list(map(int, input().split()))
    mx = v[0]
    mn = min(v[0], L - v[0])
    for i in v:
        mx = max(mx, max(i, L - i))
        mn = max(mn, min(i, L - i))
    print(mn, mx)