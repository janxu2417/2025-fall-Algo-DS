n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
tot = sum(a)
num = 0
for i in range(1, n + 1):
    num += a[i - 1]
    if num > tot - num:
        print(i)
        break