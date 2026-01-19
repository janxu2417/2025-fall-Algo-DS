def dfs(ai, n):
    tot = 0
    for i in range(ai, n + 1):
        if n % i == 0: tot += dfs(i, n // i)
        if i * i > n:
            tot += 1
            break
    return tot
t = int(input())
for _ in range(t):
    n = int(input())
    ans = dfs(2, n)
    print(ans)