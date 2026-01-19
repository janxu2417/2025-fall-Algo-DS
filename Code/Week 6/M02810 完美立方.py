from collections import defaultdict
n = int(input())
dic = defaultdict(list)
for b in range(2, n):
    for c in range(b, n):
        dic[c ** 3 + b ** 3].append(c)
ans = []
for a in range(6, n + 1):
    for d in range(5, a):
        tmp = a ** 3 - d ** 3
        if len(dic[tmp]):
            for c in dic[tmp]:
                if c < d:
                    b = (tmp - c ** 3) ** (1/3)
                    ans.append((a, round(b), c, d))
ans.sort()
for i in ans:
    a, b, c, d = i[0], i[1], i[2], i[3]
    print(f'Cube = {a}, Triple = ({b},{c},{d})')
