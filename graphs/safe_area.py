import sys
input=sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_h = max(map(max, grid))
ans = 0

for h in range(max_h):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] > h and not visited[i][j]:
                cnt += 1
                stk = [(i, j)]
                visited[i][j] = True
                while stk:
                    x, y = stk.pop()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and grid[nx][ny] > h:
                                visited[nx][ny] = True
                                stk.append((nx, ny))
                                
    ans = max(ans, cnt)
    
print(ans)