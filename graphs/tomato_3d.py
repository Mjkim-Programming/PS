from collections import deque
import sys
input=sys.stdin.readline

M, N, H = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# z x y

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque([])

for k in range(H):
    for i in range(N):
        for j in range(M):
                if grid[k][i][j] == 1:
                    q.append((k, i, j))
            
while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
            if grid[nz][nx][ny] == 0:
                grid[nz][nx][ny] = grid[z][x][y] + 1
                q.append((nz, nx, ny))
                
res = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if grid[k][i][j] == 0:
                print(-1)
                exit(0)
            res = max(res, grid[k][i][j])
        
print(res - 1)