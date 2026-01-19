p = int(input())
a = list(map(int, input().split()))
n = len(a)
a.sort()
i, j = 0, n - 1
mx = 0
num = 0
while i <= j and (p >= a[i] or num):
    while i <= j and p >= a[i]:
        p -= a[i]
        num += 1
        i += 1
    mx = max(mx, num)
    if i <= j and num:
        p += a[j]
        num -= 1
        j -= 1
print(mx)