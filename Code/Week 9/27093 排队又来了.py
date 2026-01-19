n, d = map(int, input().split())
h = list(map(int, input().split()))
q = [[h[0]]]
mns = [h[0]]
mxs = [h[0]]
for i in range(1, n):
    x = h[i]
    if mxs[-1] - d > x or x > mns[-1] + d:
        q.append([x])
        mns.append(x)
        mxs.append(x)
    else: #mxs[-1] - d <= x <= mns[-1] + d:
        j = len(q) - 1
        while j >= 0 and mxs[j] - d <= x <= mns[j] + d:
            j -= 1
        q[j + 1].append(x)
        mns[j + 1] = min(mns[j + 1], x)
        mxs[j + 1] = max(mxs[j + 1], x)
ans = []
for i in q:
    ans.extend(sorted(i))
print(*ans)