from collections import defaultdict
n = int(input())
dic = defaultdict(set)
for k in range(n):
    c = list(input().split())
    for i in range(1, len(c)):
        dic[c[i]].add(k + 1)

m = int(input())
for _ in range(m):
    x = input()
    if dic.get(x, 'default') == 'default':
        print('NOT FOUND')
    else:
        tmp = list(dic[x])
        tmp.sort()
        print(*tmp, sep = ' ')