from math import sqrt
t = 1
while True:
    n, d = map(int, input().split())
    if not n and not d: break
    a = []
    flag = 0
    for i in range(n):
        x, y = map(int, input().split())
        if y > d: flag = 1
        else:
            l = - sqrt(d ** 2 - y ** 2) + 1.0 * x
            r = sqrt(d ** 2 - y ** 2) + 1.0 * x
            a.append((l, r))
    if flag:
        print(f'Case {t}: -1')
    else:
        a.sort(key = lambda x : x[0])
        lf = a[0][0]
        rt = a[0][1]
        ans = 1
        for i in range(1, n):
            if a[i][0] <= rt:
                lf = a[i][0]
                rt = min(rt, a[i][1])
            else:
                lf = a[i][0]
                rt = a[i][1]
                ans += 1
        print(f'Case {t}: {ans}')
    _ = input()
    t += 1