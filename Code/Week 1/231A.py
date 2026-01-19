n=int(input())
ans=0
for i in range(n):
    x,y,z=map(int,input().split())
    if x+y+z>=2:
        ans+=1
print(ans)