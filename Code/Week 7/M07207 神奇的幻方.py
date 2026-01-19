n = int(input())
m = 2 * n - 1
a = [[0] * m for _ in range(m)]
i, j = 0, n - 1
a[i][j] = 1
for k in range(2, m ** 2 + 1):
    i1 = (i + m - 1) % m
    j1 = (j + 1) % m
    if a[i1][j1]:
        i1, j1 = i + 1, j
    i, j = i1, j1
    a[i][j] = k
for _ in range(m):
    print(*a[_])
