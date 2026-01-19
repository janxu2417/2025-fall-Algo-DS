def divide_up(n,a):
    return (n+a-1)//a

n,m,a=map(int,input().split())
print(divide_up(n,a)*divide_up(m,a))