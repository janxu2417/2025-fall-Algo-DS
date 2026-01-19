n=int(input())
opt=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in range(n):
    s=input()
    c=int(s[0:2])
    y=int(s[2:4])
    m=int(s[4:6])
    d=int(s[6:8])
    if m==1 or m==2:
        m+=12
        y-=1
        if y<0:
            y+=100
            c-=1
    w=((y+y//4+c//4-2*c+(26*(m+1))//10+d-1)%7+7)%7
    print(opt[w])
