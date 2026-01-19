import sys
fa = []
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

data = sys.stdin.read()
lines = data.splitlines()
i = 0
while i < len(lines):
    n, m = map(int, lines[i].split())
    i += 1
    fa = list(range(n + 1))
    for _ in range(m):
        x, y = map(int, lines[i].split())
        fx, fy = find(x), find(y)
        if fx == fy: print('Yes')
        else:
            print('No')
            fa[fy] = fx
        i += 1
    ans = []
    for j in range(1,n+1):
        if fa[j] == j: ans.append(j)
    print(len(ans))
    print(*ans)
