n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
m = (n + 1) // 2
cnt = [0] * m
for i in range(n):
    for j in range(n):
        x = min(min(i, n - 1 - i), min(j, n - 1 - j))
        cnt[x] += a[i][j]
print(max(cnt))