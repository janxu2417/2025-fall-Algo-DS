n = int(input())
a = []
for i in range(n):
    x, h = map(int, input().split())
    a.append((x, h))
ans = 1
lf = a[0][0]
for i in range(1, n - 1):
    if lf < a[i][0] - a[i][1]:
        ans += 1
        lf = a[i][0]
    elif a[i + 1][0] > a[i][0] + a[i][1]:
        ans += 1
        lf = a[i][0] + a[i][1]
    else:
        lf = a[i][0]
if n > 1: ans += 1
print(ans)