from collections import defaultdict

def sol(x):
    y = 0
    while x > 0:
        y += x % 10
        x //= 10
    return y

m, n, k = map(int, input().split(','))
dic = defaultdict(list)
for i in range(m + 1, n):
    x = sol(i)
    if x % k == 0:
        dic[x].append(str(i))
for i in sorted(dic.keys()):
    print(','.join(dic[i]))