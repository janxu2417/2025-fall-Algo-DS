a=int(input())
n,m=a//2,a//4
min,max=0,0
for i in range(0,n+1):
    if not (a-i*2)%4:
        tot=i+(a-i*2)//4
        if tot<min or not min:
            min=tot
        if tot>max:
            max=tot
print(min,max)