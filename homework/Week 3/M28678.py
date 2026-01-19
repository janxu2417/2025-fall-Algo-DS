n = int(input())
while n > 1:
    if n % 2:
        #print(n,'*3+1=',n * 3 + 1, sep='')
        print(f'{n}*3+1={n*3+1}')
        n = n * 3 + 1
    else:
        #print(n,'/2=',n//2,sep='')
        print(f'{n}/2={n//2}')
        n //= 2
print('End')