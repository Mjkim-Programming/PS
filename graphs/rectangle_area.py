import sys
input=sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N, K = map(int, input().split())
adj = [[1]*N for _ in range(M)]
for _ in range(K):
    x0, y0, x1, y1 = map(int, input().split())
    for x in range(x0, x1):
        for y in range(y0, y1):
            adj[y][x] = 0

cnt = 0
areas = []

for i in range(M):
    for j in range(N):
        if adj[i][j] == 1:
            cnt += 1
            area = 1
            stk = [(i, j)]
            adj[i][j] = 0
            while stk:
                y, x = stk.pop()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        if adj[ny][nx] == 1:
                            adj[ny][nx] = 0
                            stk.append((ny, nx))
                            area += 1
            areas.append(area)

areas.sort()
print(cnt)
print(*areas)