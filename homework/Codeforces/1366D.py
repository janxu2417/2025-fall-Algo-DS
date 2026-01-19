dic=dict()
def divide(a, prm, is_prm):
    d = []
    for x in a:
        flag = 0
        if x in dic:
            d.append((dic[x][0], dic[x][1]))
        y = x
        for i in prm:
            if i*i > x: break
            if y%i == 0:
                tmp = 1
                while y%i == 0:
                    y//=i
                    tmp *= i
                if y != 1:
                    dic[x] = (tmp, x // tmp)
                    d.append((tmp, x // tmp))
                    flag = 1
                    break
        if not flag:
            dic[x] = (-1, -1)
            d.append((-1, -1))
    return d

n = int(input())
a1 = list(map(int,input().split()))
prm=[]
is_prm=[1]*3170
for i in range(2,3170):
    if is_prm[i]: prm.append(i)
    for j in prm:
        if i*j>=3170: break
        is_prm[i*j] = 0
        if i%j == 0: break
d = divide(a1, prm, is_prm)
for i in d:
    print(i[0],end=' ')
print('')
for i in d:
    print(i[1],end=' ')