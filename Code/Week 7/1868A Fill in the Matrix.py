for _ in range(int(input())):
    n, m = map(int, input().split())
    if m == 1:
        print(*[0] * (n + 1), sep = '\n')
        continue
    s = min(n + 1, m)
    print(s)
    ans = []
    if s == m:
        vi = list(range(m))
        for i in range(1, s):
            tmp = []
            for j in range(i, i + s):
                tmp.append(j % s)
            ans.append(tmp)
        for i in range(n - s + 1):
            ans.append(ans[i % s])
    else:
        for i in range(1, s):
            tmp = []
            for j in range(i, i + s):
                tmp.append(j % s)
            tmp.extend(list(range(s, m)))
            ans.append(tmp)
    for i in range(n):
        print(*ans[i])