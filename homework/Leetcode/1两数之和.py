nums=list(map(int,input().split()))
target=int(input())

n=len(nums)
p=[]
for i in range(n):
    p.append([nums[i],i])
p.sort(key=lambda x: x[0])
for i in range(n-1):
    l=i+1
    r=n-1
    flag=0
    while l<r:
        mid=(l+r)//2
        if p[mid][0]+p[i][0]>target: r=mid-1
        elif p[mid][0]+p[i][0]<target: l=mid+1
        else:
            print([p[i][1],p[mid][1]])
            flag=1
            break
    if flag==0 and p[l][0]+p[i][0]==target:
        print([p[i][1], p[l][1]])
        flag = 1
    if flag==1: break