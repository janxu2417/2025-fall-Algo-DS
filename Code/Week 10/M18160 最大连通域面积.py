dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(x, y, n, m, a, flag):
    flag[x][y] = 1
    ans = 1
    for t in range(8):
        xn = x + dx[t]
        yn = y + dy[t]
        if xn < 0 or xn >= n or yn < 0 or yn >= m: continue
        if flag[xn][yn] or a[xn][yn] != 'W': continue
        ans += dfs(xn, yn, n, m, a, flag)
    return ans
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    flag = []
    for i in range(n):
        a.append(input())
        flag.append([0] * m)
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'W' and not flag[i][j]:
                ans = max(ans, dfs(i, j, n, m, a, flag))
    print(ans)