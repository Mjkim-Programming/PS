import sys
input=sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
adj = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
areas = []

for i in range(N):
    for j in range(M):
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
                    if 0 <= nx < M and 0 <= ny < N:
                        if adj[ny][nx] == 1:
                            adj[ny][nx] = 0
                            stk.append((ny, nx))
                            area += 1
            areas.append(area)

print(cnt)
try:
    print(max(areas))
except:
    print(0)