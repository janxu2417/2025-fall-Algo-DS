fa = []
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]
i = 1
while True:
    n, m = map(int, input().split())
    if not n and not m : break
    fa = [_ for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        fa[find(x)] = find(y)
    ans = 0
    for j in range(1,n+1):
        if fa[j] == j: ans += 1
    print(f'Case {i}: {ans}')
    i += 1