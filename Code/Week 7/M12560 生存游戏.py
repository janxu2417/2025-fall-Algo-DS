dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
def check(x, y, a):
    tot = 0
    for i in range(8):
        tot += a[x + dx[i]][y + dy[i]]
    return tot
n, m = map(int, input().split())
a = [[0] * (m + 2)]
for i in range(n):
    a.append([0] + list(map(int, input().split())) + [0])
a.append([0] * (m + 2))
ans = [[0] * m for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        num = check(i, j, a)
        if a[i][j]:
            if num == 2 or num == 3: ans[i - 1][j - 1] = 1
            else: ans[i - 1][j - 1] = 0
        else: ans[i - 1][j - 1] = 1 if num == 3 else 0
for i in range(n):
    print(*ans[i])