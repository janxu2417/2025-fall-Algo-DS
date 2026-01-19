import array
import sys
n = int(input())
a = list(map(int,input().split()))
maxA = max(a)
#spf = list(range(maxA + 1))
spf = array.array('i', range(maxA + 1))
# min prime of i
prm = array.array('i', [])
for i in range(2,maxA + 1):
    if spf[i] == i:
        prm.append(i)
    for j in prm:
        if i * j > maxA: break
        spf[i * j] = j
        if j == spf[i]: break
print(f"占用内存: {sys.getsizeof(spf) / 2 ** 20} Megabytes")
d1, d2 = [], []
for x in a:
    flag = 0
    i = spf[x]
    tmp = x
    while tmp % i == 0:
        tmp //= i
    if tmp != 1:
        d1.append(tmp)
        d2.append(x // tmp)
    else:
        d1.append(-1)
        d2.append(-1)
print(*d1, sep = ' ')
print(*d2, sep = ' ')