n = int(input())

def check(x, y):
    if x[0] >= y[0] and x[1] <= y[1]: return -1
    if x[0] <= y[0] and x[1] >= y[1]: return 1
    return 0

a = list(map(int, input().split()))
q = [(0, a[0])]
for i in range(1, n):
    li = max(0, i - a[i])
    ri = min(n - 1, i + a[i])
    while len(q) and check(q[-1], (li, ri)) == -1:
        q.pop()
    if len(q) and check(q[-1], (li, ri)) == 1: continue
    q.append((li, ri))
rt = q[0][1]
ans = 1
j = 1
while j < len(q):
    while j < len(q) and q[j][0] <= rt + 1:
        j += 1
    rt = q[j - 1][1]
    ans += 1
print(ans)