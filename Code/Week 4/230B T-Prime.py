is_prime=[1]*1000001
prm=[]
def solve():
    for i in range(2,10**6):
        if is_prime[i]:
            prm.append(i)
        for j in prm:
            if i*j>10**6: break
            is_prime[i*j]=0
            if i%j==0: break
n=int(input())
a=list(map(int,input().split()))
solve()
for i in a:
    l=0
    r=len(prm)-1
    while l<r:
        mid=(l+r)//2
        if prm[mid]**2>=i: r=mid
        else: l=mid+1
    if prm[l]**2==i: print('YES')
    else : print('NO')