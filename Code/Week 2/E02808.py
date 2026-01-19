L,M = map(int,input().split())
a = [1] * (L+1)
for i in range(M):
    x,y = map(int,input().split())
    for j in range(x,y+1):
        a[j] = 0
print(a.count(1))