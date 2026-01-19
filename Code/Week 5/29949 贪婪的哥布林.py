n, m = map(int, input().split())
a = []
for _ in range(n):
    vi, wi = map(int, input().split())
    a.append((vi, wi))
a.sort(key = lambda x : x[0] / x[1], reverse = True)
ans = 0.0
for x in a:
    if m <= x[1]:
        ans += x[0] * m / x[1]
        break
    else:
        m -= x[1]
        ans += x[0]
print(f'{ans:.2f}')