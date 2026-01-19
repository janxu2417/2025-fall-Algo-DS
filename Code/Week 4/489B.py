n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0
i, j = 0, 0
while i < n and j < m:
    if abs(a[i] - b[j]) <= 1:
        ans += 1
        i += 1
        j += 1
    elif a[i] < b[j]: i += 1
    else: j += 1
print(ans)