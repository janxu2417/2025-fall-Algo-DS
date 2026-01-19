a, b, k = map(int, input().split())
flag = [[1] * b for _ in range(a)]
for i in range(k):
    r, s, p, t = map(int, input().split())
    p = (p - 1) // 2
    r -= 1
    s -= 1
    for x in range(a):
        for y in range(b):
            if r - p <= x <= r + p and s - p <= y <= s + p:
                flag[x][y] *= t
            else: flag[x][y] *= (1 - t)
ans = 0
for i in range(a):
    ans += sum(flag[i])
print(ans)