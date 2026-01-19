s1=input()
s2=input()
ans=0
for i in range(len(s1)):
    x1=ord(s1[i])
    x2=ord(s2[i])
    if x1>=97:
        x1=x1-97+65
    if x2>=97:
        x2=x2-97+65
    if x1<x2:
        ans=-1
        break
    if x2<x1:
        ans=1
        break
print(ans)