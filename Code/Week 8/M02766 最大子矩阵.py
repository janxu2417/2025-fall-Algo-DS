import sys
it = iter(sys.stdin.read().strip().split())
n = int(next(it))
a = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i].append(int(next(it)))
ans = a[0][0]
for i in range(n):
    b = [0 for k in range(n)]
    for j in range(i, n):
        tmp = 0
        for k in range(n):
            b[k] += a[j][k]
            tmp = max(b[k], tmp + b[k])
            ans = max(ans, tmp)
print(ans)
