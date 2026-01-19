n = int(input())
a = list(map(int,input().split()))
cnt=ans=0
for i in a:
    if cnt+i >= 0: cnt += i
    else: ans+=1
print(ans)
