n, m = map(int, input().split())
inf = float('inf')
d = inf
s = []
for _ in range(n):
    x, y = map(int, input().split())
    d = min(d, x + y)
    s.append(x)
s.sort()
i = 0
ans = 0
while i < n and s[i] * 2 < d and s[i] <= m:
    m -= s[i]
    i += 1
    ans += 1
ans += m // d * 2
m %= d
if i < n and s[i] <= m:
    m -= s[i]
    i += 1
    ans += 1
if i > 0 and s[i - 1] + m >= d:
    ans += 1
print(ans)