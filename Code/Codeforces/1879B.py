t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=-1
    x=sum(a)+n*min(b)
    y=sum(b)+n*min(a)
    print(min(x,y))
    t-=1