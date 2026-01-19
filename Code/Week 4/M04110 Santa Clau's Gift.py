from functools import cmp_to_key
def compare(x, y):
    return -1 if x[0] * y[1] > y[0] * x[1] else 1
n, w = map(int, input().split())
a = []
for _ in range(n):
    vi, wi = map(int, input().split())
    a.append((vi, wi))
a.sort(key = cmp_to_key(compare))
ans = 0.0
for i in a:
    if i[1] <= w:
        ans += i[0]
        w -= i[1]
    else:
        ans += i[0] * w / i[1]
        break
print(f'{ans:.1f}')