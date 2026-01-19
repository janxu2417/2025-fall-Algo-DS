def dfs(n, a, b, c):
    if n == 1:
        print(f'1:{a}->{c}')
        return
    dfs(n - 1, a, c, b)
    print(f'{n}:{a}->{c}')
    dfs(n - 1, b, a, c)
    return
s = input().split()
n = int(s[0])
a, b, c = s[1], s[2], s[3]
dfs(n, a, b, c)