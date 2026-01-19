a = []
for i in range(5):
    a.append(list(map(int, input().split())))

def check(res):
    b = [[0] + res[:] + [0]]
    for i in range(5):
        c = []
        for j in range(1, 7):
            c.append((a[i][j - 1] + b[i][j - 1] + b[i][j] + b[i][j + 1]) % 2)
            if i > 0:
                c[j - 1] = (c[j - 1] + b[i - 1][j]) % 2
        b.append([0] + c + [0])
    if sum(b[5]) == 0:
        for i in range(5):
            print(*b[i][1:7])
    return
def dfs(pos, tmp):
    if pos == 6:
        check(tmp)
        return
    tmp[pos] = 1
    dfs(pos + 1, tmp)
    tmp[pos] = 0
    dfs(pos + 1, tmp)

tmp = [0] * 6
dfs(0, tmp)