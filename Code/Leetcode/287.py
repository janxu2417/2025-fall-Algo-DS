nums=list(map(int,input().split()))
n=len(nums)-1
l,r=1,n
while l<r:
    mid=(l+r)//2
    cnt=0
    for i in range(n+1):
        if nums[i]<=mid: cnt+=1
    if cnt<=mid: l=mid+1
    else: r=mid
print(l)
#return l
