from heapq import heappush, heappop
import sys
def bfs(m, n, wh, q, xj, yj):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        h, x, y = heappop(q)
        h = -h
        if x == xj and y == yj:
            return True
        if h < wh[x][y]: continue
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if h > wh[nx][ny]:
                wh[nx][ny] = h
                heappush(q, (-h, nx, ny))
    return False
def main():
    data = sys.stdin.read().split() #数据一次性读入
    it = iter(data)
    out = []
    for _ in range(int(next(it))):
        m = int(next(it))
        n = int(next(it))
        h = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(int(next(it)))
            h.append(tmp)
        water_height = [h[i][:] for i in range(m)]
        xj = int(next(it)) - 1
        yj = int(next(it)) - 1
        q = []
        for i in range(int(next(it))):
            xi = int(next(it)) - 1
            yi = int(next(it)) - 1
            heappush(q, (-h[xi][yi], xi, yi)) #将所有起点放入大顶堆中
        if bfs(m, n, water_height, q, xj, yj):
            out.append('Yes')
        else:
            out.append('No')
    print('\n'.join(out))
if __name__ == '__main__':
    main()
