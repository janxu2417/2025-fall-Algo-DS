def solve(mx, my, x, y):
    for i in range(y):
        if (mx - my + x * i) % y == 0:
            return mx + x * i
p, e, i, d = map(int, input().split())
#23 28 33
p %= 23
e %= 28
i %= 33
x = solve(p, e, 23, 28)
y = solve(x, i, 23 * 28, 33)
if y <= d: y += 21252
print(y - d)