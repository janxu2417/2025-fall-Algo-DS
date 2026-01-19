while True:
    a=list(map(int,input().split()))
    ans=a[5]+a[4]+a[3]
    a[0]=max(0,a[0]-a[4]*11) # NO.5+NO.1 complete
    if a[1]>=a[3]*5:
        a[1]-=a[3]*5 # NO.4+NO.2 complete
    else:
        a[0]=max(0,a[0]-(a[3]*5-a[1])*4) #NO.4+NO.2 completed + NO.1
        a[1]=0
    ans+=a[2]//4
    if a[2]%4:# NO.3 complete
        tmp=7-(a[2]%4)*2
        ans+=1
        if a[1]>=tmp:
            a[1]-=tmp
            a[0]=max(0,a[0]-36+(a[2]%4)*9+tmp*4)
        else:
            a[0] = max(0, a[0] - 36 + (a[2] % 4) * 9 + a[1] * 4)
            a[1]=0
    ans+=a[1]//9
    if a[1]%9:
        ans+=1
        a[0]=max(0,a[0] - 36 + a[1] % 9 *4)
    ans+=a[0]//36+(a[0]%36>0)
    if not ans: break
    print(ans)