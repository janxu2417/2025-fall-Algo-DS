from heapq import heappush, heappop
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
inf = float('inf')
def dijkstra(sx, sy, tx, ty):
    if h[sx][sy] == '#' or h[tx][ty] == '#': return inf
    q = []
    d = [[inf] * n for _ in range(m)]
    d[sx][sy] = 0
    heappush(q, (0, sx, sy))
    while q:
        dist, ux, uy = heappop(q)
        if d[ux][uy] != dist: continue
        if (ux, uy) == (tx, ty): return dist
        for t in range(4):
            nx, ny = ux + dx[t], uy + dy[t]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if h[nx][ny] == '#': continue
            now_dist = dist + abs(int(h[ux][uy]) - int(h[nx][ny]))
            if now_dist >= d[nx][ny]: continue
            d[nx][ny] = now_dist
            heappush(q, (now_dist, nx, ny))
    return d[tx][ty]
m, n, p = map(int, input().split())
h = []
for _ in range(m):
    h.append(input().split())
for _ in range(p):
    sx, sy, tx, ty = map(int, input().split())
    min_d = dijkstra(sx, sy, tx, ty)
    if min_d == inf: print('NO')
    else: print(min_d)
