from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque([])
        d = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    d[i][j] = 0
                    q.append((i, j))
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while q:
            x, y = q.popleft()
            for t in range(4):
                nx, ny = x + dx[t], y + dy[t]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
        return d
if __name__ == '__main__':
    sol = Solution
    mat = []
