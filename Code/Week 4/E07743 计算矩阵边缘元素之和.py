a = []
m, n = map(int, input().split())
tot = 0
for _ in range(m):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            tot += a[i][j]
print(tot)