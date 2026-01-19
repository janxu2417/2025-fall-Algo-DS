n, k = map(int, input().split())
a = list(map(int, input().split()))
def dfs(i, x, tmp, ans):
    if i == k:
        ans.append(tmp[:])
        return
    opt = set()
    for j in range(x, n - k + i + 1):
        if a[j] not in opt:
            tmp.append(a[j])
            dfs(i + 1, j + 1, tmp, ans)
            tmp.pop()
            opt.add(a[j])
    return
ans = []
dfs(0, 0, [], ans)
for i in ans:
    print(*i)