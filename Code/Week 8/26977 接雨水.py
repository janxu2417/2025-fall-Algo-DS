n = int(input())
h = list(map(int, input().split()))
stack = [0]
ans = 0
for i in range(1, n):
    while stack and h[stack[-1]] < h[i]:
        index = stack.pop()
        if stack: ans += (min(h[stack[-1]], h[i]) - h[index]) * (i - stack[-1] - 1)
    stack.append(i)
print(ans)