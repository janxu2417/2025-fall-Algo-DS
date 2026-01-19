n, d = map(int, input().split())
a = sorted(list(map(int, input().split())))
flag = 0
for i in range(n):
    if a[2 * i + 1] - a[2 * i] > d:
        flag = 1
        break
print('Yes' if flag == 0 else 'No')