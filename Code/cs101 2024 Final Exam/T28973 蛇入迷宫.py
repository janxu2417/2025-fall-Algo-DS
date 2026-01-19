from collections import deque
def check(x, y, z, n, m):
    if z == 0: return y < n - 1 and m[x][y] | m[x][y + 1] == 0
    return x < n - 1 and m[x][y] | m[x + 1][y] ==0
def main():
    n = int(input())
    m = []
    for _ in range(n):
        m.append(list(map(int, input().split())))
    q = deque([(0, 0, 0, 0)])
    inf = float('inf')
    dist = [[[inf, inf] for j in range(n)] for i in range(n)]
    dist[0][0][0] = 0
    dx = [1, 0, 0, 0]
    dy = [0, 1, 0, 0]
    dz = [0, 0, 1, -1]
    while q:
        x, y, z, d = q.popleft()
        if d != dist[x][y][z]: continue
        for t in range(4):
            nx, ny, nz = x + dx[t], y + dy[t], z + dz[t]
            if nx < n and ny < n and 0 <= nz < 2 and check(nx, ny, nz, n, m):
                if dz[t] and m[x + 1][y + 1]: continue
                nd = d + 1
                if nd < dist[nx][ny][nz]:
                    dist[nx][ny][nz] = nd
                    q.append((nx, ny, nz, nd))
    print(dist[n - 1][n - 2][0] if dist[n - 1][n - 2][0] != inf else -1)
if __name__ == '__main__':
    main()
