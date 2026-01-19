
a=int(input())
b=int(input())
c=str(a+b)
i=0
while i < len(c) and c[i]=='0': i+=1
if i==len(c): print('0')
while i<len(c):
    print(c[i],end='')
    i+=1
