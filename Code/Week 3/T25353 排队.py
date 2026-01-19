n, d = map(int, input().split())
ans = []
q = []
for i in range(n):
    q.append([int(input()), i + 1])
q[n-1][1] = 0
start = 0
tail = n - 1
m = n
while m:
    tmp = []
    mn = q[start][0]
    mx = q[start][0]
    i = start
    s1 = start
    t1 = tail
    flag = 0
    i = start
    for _ in range(m):
        x = q[i][0]
        if x >= mx - d and x <= mn + d:
            tmp.append(x)
        else:
            if not flag:
                s1 = i
                t1 = i
                flag = 1
            else:
                q[t1][1] = i
                t1 = i
        mn = min(mn, x)
        mx = max(mx, x)
        if mx - mn > d * 2:
            q[t1][1] = q[i][1]
            break
        i = q[i][1]
    start = s1
    tail = t1
    m -= len(tmp)
    ans.extend(sorted(tmp))

for i in ans: print(i)