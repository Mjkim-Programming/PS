import sys
input=sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

w, h = map(int, input().split())
while (w, h) != (0, 0):
    cnt = 0
    grid = [[0]*h for _ in range(w)]
    for y in range(h):
        row = list(map(int, input().split()))
        for x in range(w):
            grid[x][y] = row[x]
    visited = [[False]*h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            if grid[i][j] == 1 and not visited[i][j]:
                cnt += 1
                stk = [(i, j)]
                visited[i][j] = True
                while stk:
                    x, y = stk.pop()
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < w and 0 <= ny < h:
                            if not visited[nx][ny] and grid[nx][ny] == 1:
                                visited[nx][ny] = True
                                stk.append((nx, ny))
    print(cnt)
    w, h = map(int, input().split())