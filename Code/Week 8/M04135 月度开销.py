n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
def check(x):
    tot = 0
    cnt = 1
    for i in range(n):
        if tot + a[i] > x:
            cnt += 1
            tot = a[i]
        else: tot += a[i]
        if cnt > m: return False
    return cnt <= m
l, r = max(a), sum(a)
while l < r:
    mid = (l + r) // 2
    if check(mid): r = mid
    else: l = mid + 1
print(r)