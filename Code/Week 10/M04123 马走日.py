dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
def dfs(k, flag, x, y, n, m):
    if k == n * m:
        return 1
    ans = 0
    for t in range(8):
        xn = x + dx[t]
        yn = y + dy[t]
        if xn < 0 or xn >= n or yn < 0 or yn >= m: continue
        if flag[xn][yn]: continue
        flag[xn][yn] = 1
        ans += dfs(k + 1, flag, xn, yn, n, m)
        flag[xn][yn] = 0
    return ans
for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    flag = [[0] * m for i in range(n)]
    flag[x][y] = 1
    print(dfs(1, flag, x, y, n, m))