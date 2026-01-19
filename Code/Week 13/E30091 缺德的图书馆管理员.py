l = int(input())
n = int(input())
mn, mx = 0, 0
a = list(map(int, input().split()))
for i in a:
    mn = max(mn, min(i, l + 1 - i))
    mx = max(mx, max(i, l + 1 - i))
print(mn, mx)