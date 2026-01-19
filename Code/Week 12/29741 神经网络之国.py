n, l, m = map(int, input().split())
mod = 10 ** 9 + 7

def times(a, b):
    c = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c

def quicktimes(mt, x):
    tmp = [[0] * m for _ in range(m)]
    for i in range(m):
        tmp[i][i] = 1
    while x > 0:
        if x % 2: tmp = times(tmp, mt)
        mt = times(mt, mt)
        x >>= 1
    return tmp

dp = [0] * m
a = list(map(int, input().split()))
for i in a:
    dp[i % m] += 1
c = list(map(int, input().split()))
cl = list(map(int, input().split()))
mt = [[0] * m]
for i in c:
    mt[0][-i % m] += 1
for i in range(1, m):
    mt.append([mt[i - 1][-1]] + mt[i - 1][:m - 1])
tmp = quicktimes(mt, l - 2)
dps = [0] * m
for i in range(m):
    for j in range(m):
        dps[i] = (dps[i] + tmp[i][j] * dp[j]) % mod
ans = 0
for i in range(n):
    ans = (ans + dps[(-c[i] - cl[i]) % m]) % mod
print(ans)