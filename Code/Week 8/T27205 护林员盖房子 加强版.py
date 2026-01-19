def solve(h, n):
    mx = 0
    stack = [0]
    for i in range(1, n):
        while stack and h[stack[-1]] > h[i]:
            index = stack.pop()
            l = index
            if stack: l = stack[-1] + 1
            mx = max(mx, h[index] * (i - l))
        stack.append(i)
    return mx

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
h = [0] * (n + 2)
ans = 0
for i in range(m):
    for j in range(n):
        if a[i][j]: h[j + 1] = 0
        else: h[j + 1] += 1
    ans = max(ans, solve(h, n + 2))
print(ans)