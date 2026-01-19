n, d = map(int, input().split())
ans = []
q = []
for i in range(n):
    q.append([int(input()), i - 1, i + 1]) # hi,pre,next
start = 0
tail = n
while start != tail:
    tmp = []
    mn = q[start][0]
    mx = q[start][0]
    flag = 0
    i = start
    while i != tail:
        x = q[i][0]
        if mx - d <= x <= mn + d:
            tmp.append(x)
            if i == start:
                start = q[i][2]
            else:
                q[q[i][1]][2] = q[i][2]
                if q[i][2] == tail:
                    tail = i
                else:
                    q[q[i][2]][1] = q[i][1]
        mn = min(mn, x)
        mx = max(mx, x)
        if mx - mn > d * 2:
            break
        i = q[i][2]
    ans.extend(sorted(tmp))
print(*ans, sep='\n')