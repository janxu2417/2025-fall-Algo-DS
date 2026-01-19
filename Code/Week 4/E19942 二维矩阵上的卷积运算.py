m, n, p, q = map(int, input().split())
a, b = [], []
for _ in range(m):
    a.append(list(map(int, input().split())))
for _ in range(p):
    b.append(list(map(int, input().split())))
for i in range(m + 1 - p):
    c = [0] * (n + 1 - q)
    for j in range(n + 1 - q):
        for k in range(p):
            for t in range(q):
                c[j] += a[i + k][j + t] * b[k][t]
    print(*c, sep = ' ')