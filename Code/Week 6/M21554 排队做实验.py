n = int(input())
t = list(map(int, input().split()))
a = []
for i in range(n):
    a.append((t[i], i + 1))
a.sort()
ans = 0
result = []
for i in range(n):
    result.append(a[i][1])
    ans += a[i][0] * (n - i - 1)
print(*result)
print(f'{ans / n:.2f}')