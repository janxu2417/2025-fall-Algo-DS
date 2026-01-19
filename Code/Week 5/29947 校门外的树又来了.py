L, M = map(int, input().split())
a = []
for _ in range(M):
    li, ri = map(int, input().split())
    a.append((li, ri))
a.sort(key = lambda x : x[0] * L + x[1])
j, ans = 1, 0
lf, rt = a[0][0], a[0][1]
while j < M:
    if a[j][0] <= rt + 1:
        rt = max(rt, a[j][1])
    else:
        ans += rt - lf + 1
        lf, rt = a[j][0], a[j][1]
    j += 1
ans += rt - lf + 1
print(L + 1 - ans)