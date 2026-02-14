from collections import deque
import sys
input=sys.stdin.readline

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([])

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            q.append((i, j))
            
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx, ny))
                
res = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(-1)
            exit(0)
        res = max(res, grid[i][j])
        
print(res - 1)