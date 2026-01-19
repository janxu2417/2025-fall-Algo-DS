n, m = map(int, input().split())
a = [[0] * (m + 2)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(sx, sy, x, y, t):
    if sx == x and sy == y and t == 3:
        return 1
    xn, yn = x + d[t][0], y + d[t][1]
    if a[xn][yn] == 0: # turn right
        return dfs(sx, sy, x, y, (t + 1) % 4) + 1
    t1 = (t + 3) % 4
    xl, yl = xn + d[t1][0], yn + d[t1][1]
    if a[xl][yl] == 1: # turn left
        return dfs(sx, sy, xl, yl, t1) + 1
    # go straight
    return dfs(sx, sy, xn, yn, t) + 1
for i in range(n):
    row = [0]
    row.extend(list(map(int, input().split())))
    row.append(0)
    a.append(row)
a.append([0] * (m + 2))
flag = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j]:
            print(dfs(i, j, i, j, 0))
            flag = 1
            break
    if flag: break
