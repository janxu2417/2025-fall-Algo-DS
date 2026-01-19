a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

yushu='1,0,X,9,8,7,6,5,4,3,2'.split(',')

n = int(input())
for i in range(n):
    s = input()
    num = 0
    for j in range(17):
        num += a[j] * int(s[j])
    num %= 11
    print('YES' if s[-1] == yushu[num] else 'NO')
