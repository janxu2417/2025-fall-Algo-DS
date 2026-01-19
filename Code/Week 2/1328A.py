import math
t=int(input())
while t :
    a,b=map(int,input().split())
    t-=1
    print((b-a%b)%b)
