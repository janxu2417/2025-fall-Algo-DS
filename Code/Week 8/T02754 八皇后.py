def check(x, s):
    for k in range(len(s)):
        if abs(int(s[k]) - x) == len(s) - k: return False
    return True
def dfs(i, n, s, flag, ans):
    if i == n:
        ans.append(s[:])
        return
    for j in range(1, n + 1):
        if not flag[j] and check(j, s):
            flag[j] = 1
            dfs(i + 1, n, s + str(j), flag, ans)
            flag[j] = 0
    return
ans = []
flag = [0] * 9
dfs(0, 8, '', flag, ans)
for _ in range(int(input())):
    print(ans[int(input()) - 1])