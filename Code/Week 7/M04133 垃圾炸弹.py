d = int(input())
n = int(input())
a = [[0] * 1025 for _ in range(1025)]
mx = 0
for i in range(n):
    x, y, m = map(int, input().split())
    for j in range(max(0, x - d), min(1025, x + d + 1)):
        for k in range(max(0, y - d), min(1025, y + d + 1)):
            a[j][k] += m
            mx = max(mx, a[j][k])
ans = 0
for j in range(1025):
    for k in range(1025):
        if a[j][k] == mx: ans += 1
print(ans, mx, sep = ' ')