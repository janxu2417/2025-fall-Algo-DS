from collections import deque
def main():
    for _ in range(int(input())):
        r, c, k = map(int, input().split())
        maze = []
        inf = float('inf')
        dist = [[[inf] * k for j in range(c)] for i in range(r)]
        for i in range(r):
            maze.append(input())
        sx, sy = -1, -1
        for i in range(r):
            for j in range(c):
                if maze[i][j] == 'S':
                    sx, sy = i, j
                    break
        dist[sx][sy][0] = 0
        q = deque([(sx, sy, 0)])
        def bfs():
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            while q:
                x, y, t = q.popleft()
                for z in range(4):
                    nx, ny, nt = x + dx[z], y + dy[z], (t + 1) % k
                    if 0 <= nx < r and 0 <= ny < c and (nt == 0 or maze[nx][ny] != '#'):
                        if dist[nx][ny][nt] > dist[x][y][t] + 1:
                            dist[nx][ny][nt] = dist[x][y][t] + 1
                            if maze[nx][ny] == 'E':
                                return str(dist[nx][ny][nt])
                            q.append((nx, ny, nt))
            return 'Oop!'
        print(bfs())

if __name__ == '__main__':
    main()