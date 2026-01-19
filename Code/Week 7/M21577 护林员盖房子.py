m, n = map(int, input().split())
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))
ans = 0
for i in range(m):
    for j in range(n):
        if a[i][j]: continue
        mx = n - j
        for k in range(i, m):
            if a[k][j]: break
            for t in range(j, mx + j):
                if a[k][t]:
                    mx = t - j
                    break
                ans = max(ans, (k - i + 1) * (t - j + 1))
print(ans)