dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y, n, m, flag, c):
    for k in range(4):
        x1, y1 = x + dx[k], y + dy[k]
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n: continue
        if m[x1][y1] != c or flag[x1][y1]: continue
        flag[x1][y1] = 1
        dfs(x1, y1, n, m, flag, c)
    return
for _ in range(int(input())):
    n = int(input())
    m = []
    for i in range(n):
        m.append(input())
    ans = [0, 0]
    flag = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] != '#' and not flag[i][j]:
                flag[i][j] = 1
                dfs(i, j, n, m, flag, m[i][j])
                if m[i][j] == 'r' : ans[0] += 1
                else : ans[1] += 1
    print(*ans)