n = int(input())
a = list(map(int, input().split()))
x = 0
mn = 0
for i in a:
    x += i
    mn = min(mn, x)
print(1 - mn)