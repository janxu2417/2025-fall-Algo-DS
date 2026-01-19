n = int(input())
a = list(map(int, input().split()))
def dfs(i, tmp, flag, ans):
    if i == n:
        ans.append(tmp[:])
        return
    opt = set()
    for j in range(n):
        if not flag[j] and a[j] not in opt:
            flag[j] = 1
            tmp.append(a[j])
            dfs(i + 1, tmp, flag, ans)
            flag[j] = 0
            tmp.pop()
            opt.add(a[j])
    return
ans = []
flag = [0] * n
dfs(0, [], flag, ans)
for i in ans:
    print(*i)