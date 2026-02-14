from collections import deque
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
adj = [list(map(int, input().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

deq = deque([(0, 0)])
visited = [[False]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]
dist[0][0] = 1
visited[0][0] = True
while deq:
    y, x = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < N and 0 <= nx < M:
            if adj[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1
                    deq.append((ny, nx))

print(dist[N-1][M-1])