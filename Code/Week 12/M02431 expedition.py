import heapq
n = int(input())
a = []
for _ in range(n):
    a.append(tuple(map(int, input().split())))
a.sort(reverse = True)
a.append((0, 0))
n += 1
l, p = map(int, input().split())
q = []
i = 0
ans = 0
while i < n:
    while i < n and p >= l - a[i][0]:
        heapq.heappush(q, -a[i][1])
        i += 1
    if i < n:
        if q:
            p += -heapq.heappop(q)
            ans += 1
        else:
            ans = -1
            break
print(ans)